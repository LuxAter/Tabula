from data.entry import Entry

class CppParser:

    def clean_comment(self, comment):
        lines = comment.split('\n')
        for index, line in enumerate(lines):
            line = line.strip()
            if line.startswith('* '):
                line = line[2:]
            elif line.startswith('/**'):
                line = line[3:]
            if line.endswith('*/'):
                line = line[:-2]
            lines[index] = line
        if lines[0] == str():
            lines = lines[1:]
        if lines[-1] == str():
            lines = lines[:-1]
        comment = '\n'.join(lines)
        return comment


    def generate_entry(self, cursor):
        doc = Entry()
        doc.name = cursor.spelling
        doc.source_file = "(null)"
        if type(cursor.raw_comment) == str:
            doc.raw_comment = self.clean_comment(cursor.raw_comment)
        doc.parse_comment()
        if doc.doc['content'] == '\n':
            print(doc.name, "is undocumented!")
        for child in cursor.get_children():
            doc.sub_entries.append(self.generate_entry(child))
        return doc

    def generate_tree(self, trans_unit):
        unit_doc = Entry()
        unit_doc.name = trans_unit.spelling
        unit_doc.source_file = trans_unit.spelling
        for child in trans_unit.cursor.get_children():
            unit_doc.sub_entries.append(self.generate_entry(child))
        return unit_doc

    def get_trans_unit(self, file):
        from clang import cindex
        lib_name = "/usr/lib/llvm-5.0/lib/libclang.so"
        cindex.Config.set_library_file(lib_name)
        index = cindex.Index.create()
        trans_unit = index.parse(file)
        if not trans_unit:
            raise ValueError("Unable to parse input file", file)
        return trans_unit
