"""
C++ Documentation Parser

:author: Arden Rasmussen
"""

from data.entry import Entry
from clang.cindex import CursorKind
from clang import cindex
import linecache


class CppParser(object):
    """
    The main parsing system for C++ files. It utilizes *Clang* to parse the AST.
    """

    def __init__(self):
        pass

    @staticmethod
    def kind_string(cursor_kind):
        """Gets string representation of the cursor kind value.

        :param cursor_kind: Cursor kind to determine string representation.

        :returns: String representation of cursor.
        """
        string = repr(cursor_kind)[11:]
        if string.lower().find('class') != -1:
            string = "CLASS"
        elif string.lower().find('function') != -1:
            string = "FUNCTION"
        return string

    @staticmethod
    def read_doc(cursor):
        """Determins if the documentation should be read.

        :param cursor: Cursor to check

        :returns: `True` if documentation should be read, `False` if it shoulden't.
        """
        if cursor.is_definition() is False:
            return False
        elif cursor.kind == CursorKind.TEMPLATE_TYPE_PARAMETER:
            return False
        elif cursor.kind == CursorKind.PARM_DECL:
            return False
        elif cursor.kind == CursorKind.TEMPLATE_NON_TYPE_PARAMETER:
            return False
        return True

    @staticmethod
    def clean_comment(comment):
        """
        Cleans the comment parsed from the C++ code, removing `/*`, `*`, `*/`, and `//`, from
        the string.

        :param comment: String representation of comment.

        :returns: Comment without escape characters.
        """
        lines = comment.split('\n')
        for index, line in enumerate(lines):
            line = line.strip()
            if line.startswith('* '):
                line = line[2:]
            elif line.startswith('/**'):
                line = line[3:]
            if line.endswith('*/'):
                line = line[:-2]
            if line == '*':
                line = ''
            lines[index] = line
        if lines[0] == str():
            lines = lines[1:]
        if lines[-1] == str():
            lines = lines[:-1]
        comment = '\n'.join(lines)
        return comment

    def get_raw_code(self, cursor):
        """
        Gets the raw code of the cursors representation.

        :param cursor: Cursor to retreave source code of.

        :returns: Pair of source file, line, and range if applicable.
        """
        loc = cursor.location
        extent = cursor.extent
        i = min(extent.start.line, loc.line)
        line = str()
        while True and i <= extent.end.line:
            new_line = linecache.getline(loc.file.name, i)
            i += 1
            new_line = new_line.rstrip()
            if new_line.endswith('{'):
                new_line = new_line[:-1]
                if self.kind_string(cursor.kind) == "CLASS":
                    line += new_line
                    break
            new_line = new_line.rstrip()
            if new_line.endswith(')'):
                line += new_line
                break
            line += new_line + "\n"
        lines = str()
        for i in range(extent.start.line, extent.end.line + 1):
            lines += linecache.getline(loc.file.name, i)
        return ["cpp", loc.file.name, line.strip(), lines.strip()]

    def read_metadata(self, cursor):
        """
        Gets the metadata of the provided cursor.

        :param cursor: Cursor to get metadata for.

        :returns: Metadata of the cursor object.
        """
        metadata = dict()
        #  metadata["result"] = cursor.result_type.spelling
        metadata["const"] = cursor.is_const_method()
        metadata["pure virtual"] = cursor.is_pure_virtual_method()
        metadata["static"] = cursor.is_static_method()
        metadata["virtual"] = cursor.is_virtual_method()
        return metadata

    def generate_entry(self, cursor, scope=None, file_path=None):
        """
        Generates an entry for the current cursor, including name, scope, comment, and any sub
        declarations.

        :param cursor: Cursor to generate comment for.
        :param scope: List of different scoping elements.

        :returns: Entry representing the current cursor.
        """
        if file_path is not None and cursor.location.file.name != file_path:
            return None
        elif file_path is None:
            file_path = cursor.location.file
        if scope is None:
            scope = list()
        doc = Entry()
        doc.name = cursor.spelling
        doc.kind = self.kind_string(cursor.kind)
        doc.usr = scope[:]
        doc.metadata = self.read_metadata(cursor)
        doc.source = self.get_raw_code(cursor)
        if isinstance(cursor.raw_comment, str):
            doc.raw_comment = self.clean_comment(cursor.raw_comment)
        doc.parse_comment()
        if doc.doc['content'] == '\n':
            pass
            #  print(doc.name, "is undocumented!")
        #  print("  " * len(scope), doc.name)
        scope.append(doc.name)
        for child in cursor.get_children():
            #  print("  " * len(scope), child.spelling)
            if self.read_doc(child) is True:
                sub_entry = self.generate_entry(child, scope, file_path)
                if sub_entry.kind not in doc.sub_entries:
                    doc.sub_entries[sub_entry.kind] = [sub_entry]
                else:
                    doc.sub_entries[sub_entry.kind].append(sub_entry)
        scope.pop()
        return doc

    def draw(self, cursor, indent):
        if cursor.spelling or cursor.displayname is not str():
            print((" | " * (indent - 1)) + " +-{} ({})".format(cursor.spelling or cursor.displayname, str(cursor.kind).split(".")[1]))
            for child in cursor.get_children():
                self.draw(child, indent + 1)


    def generate_tree(self, trans_unit):
        """
        Generates entry tree for given transition unit.

        :param trans_unit: Transition unit to generate entry tree for.

        :returns: Tree containing entries for all elements and sub elements of the transition unit.
        """
        unit_doc = Entry()
        unit_doc.name = trans_unit.spelling
        unit_doc.source_file = trans_unit.spelling
        self.draw(trans_unit.cursor, 0)
        for child in trans_unit.cursor.get_children():
            sub_entry = self.generate_entry(child, None, trans_unit.spelling)
            if sub_entry is not None:
                if sub_entry.kind not in unit_doc.sub_entries:
                    unit_doc.sub_entries[sub_entry.kind] = [sub_entry]
                else:
                    unit_doc.sub_entries[sub_entry.kind].append(sub_entry)
        return unit_doc

    @staticmethod
    def get_trans_unit(file_path):
        """
        Gets the transition unit associated with provided file.

        :param file: Path to file to determin the transition unit of.

        :returns: Transition unit of given file.
        """
        lib_name = "/usr/lib/llvm-5.0/lib/libclang.so"
        cindex.Config.set_library_file(lib_name)
        index = cindex.Index.create()
        trans_unit = index.parse(file_path)
        if not trans_unit:
            raise ValueError("Unable to parse input file", file_path)
        return trans_unit
