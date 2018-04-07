import os
from os import path

from tabula.block import Type, Block

class Parser(object):
    def __init__(self, directory):
        self.directory_path = directory
        self.recursive = False
        self.blocks = ['func', 'param', 'return']


    @staticmethod
    def indent(line):
        return len(line) - len(line.lstrip())

    def block(self, lines, index=0):
        new = Block()
        new.set_meta(lines[index].strip())
        lb = list()
        for line in lines[index+1:]:
            if self.indent(line) < 2:
                break
            lb.append(line[2:])
            index += 1
        i = 0
        while i < len(lb):
            if lb[i][0] == '@' and lb[i].strip().split()[0][1:] in self.blocks:
                tmp, i = self.block(lb, i)
                new.append(tmp)
            else:
                new.append(lb[i].strip())
            i += 1
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
        for file in files:
            self.parse_file(file)

    def parse_file(self, f):
        with open(f, 'r') as file:
            lines = file.read().splitlines()
        if lines[0].lstrip()[0] == '@' and lines[0].strip().split()[0][1:] in self.blocks:
            result, i = self.block(lines)
            print(result)

    def parse(self):
        self.parse_directory(self.directory_path)
