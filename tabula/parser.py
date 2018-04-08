import os
from os import path

from tabula.block import Type, Block
from tabula.text import Format, Text


class Parser(object):
    def __init__(self, directory):
        self.directory_path = directory
        self.recursive = False
        self.blocks = ['func', 'param', 'return']

    @staticmethod
    def indent(line):
        return len(line) - len(line.lstrip())

    def parse_text(self, line, base=Format.TEXT):
        delims = [('`', Format.CODE), ('**', Format.BOLD), ('__', Format.BOLD),
                  ('*', Format.ITALIC), ('_', Format.ITALIC), ('$', Format.MATH)]

        def in_delim(char, next_char, index=None):
            if base == Format.CODE or base == Format.MATH:
                return False, ('', Format.NONE)
            for delim in delims:
                if char == delim[0][0] and (len(delim[0]) == 1 or
                                            (len(delim[0]) == 2
                                             and next_char == delim[0][1])):
                    if index is not None and delim == index:
                        return True, delim
                    elif index is None:
                        return True, delim
            return (False, ('', Format.NONE))

        def get_next(line, index):
            if index + 1 >= len(line):
                return None
            else:
                return line[index + 1]

        delim_stack = list()
        new = Text()
        new.type = base
        current = str()
        i = 0
        while i < len(line):
            if line[i] == '@':
                future = line[i:]
                if future.startswith('@ref '):
                    new.append(current)
                    current = str()
                    i += 5
                    ref_id = line[i:].split()[0]
                    i += len(ref_id)
                    ref = Text()
                    ref.type = Format.REF
                    ref.metadata = [ref_id]
                    new.append(ref)
            if in_delim(line[i], get_next(line, i))[0]:
                delim = in_delim(line[i], get_next(line, i))[1]
                new.append(current)
                current = str()
                i += len(delim[0])
                while i < len(line) and not in_delim(line[i], get_next(
                        line, i), delim)[0]:
                    current += line[i]
                    i += 1
                new.append(self.parse_text(current, delim[1]))
                current = str()
                i += len(delim[0]) - 1
            else:
                current += line[i]
            i += 1
        new.append(current)
        return new

    def block(self, lines, index=0):
        new = Block()
        new.set_meta(lines[index].strip())
        lb = list()
        for line in lines[index + 1:]:
            if self.indent(line) < 2:
                break
            lb.append(line[2:])
            index += 1
        i = 0
        while i < len(lb):
            if lb[i][0] == '@' and lb[i].strip().split()[0][1:] in self.blocks:
                tmp, i = self.block(lb, i)
                if new.data and isinstance(new.data[-1], str):
                    new.data[-1] = self.parse_text(new.data[-1])
                new.append(tmp)
            else:
                new.append(lb[i].strip())
            i += 1
        if new.data and isinstance(new.data[-1], str):
            new.data[-1] = self.parse_text(new.data[-1])
        return new, index

    def parse_directory(self, d):
        dirs = [
            os.path.join(d, o) for o in os.listdir(d)
            if os.path.isdir(os.path.join(d, o))
        ]
        files = [
            os.path.join(d, o) for o in os.listdir(d)
            if os.path.isfile(os.path.join(d, o))
        ]
        result = []
        for file in files:
            result.append(self.parse_file(file))
        return result

    def parse_file(self, f):
        with open(f, 'r') as file:
            lines = file.read().splitlines()
        if lines[0].lstrip()[0] == '@' and lines[0].strip().split(
        )[0][1:] in self.blocks:
            result, i = self.block(lines)
            return result
        return None

    def parse(self):
        return self.parse_directory(self.directory_path)
