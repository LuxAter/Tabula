"""C++ Parser"""

from parsers.cpp.types import Typenames
from pprint import pprint
import re


class CppParser:

    def __init__(self):
        self.data = list()

    def read(self, file_path):
        with open(file_path) as file:
            in_comment = False
            ended_comment = False
            entry = [list(), str()]
            scope = list()
            for line in file:
                if line.strip().startswith("/**") or line.strip().startswith(
                        "/*!"):
                    in_comment = True
                    entry = [list(), str()]
                if in_comment is True:
                    if self.clean(line) is not None:
                        entry[0].append(self.clean(line))
                if line.strip().startswith("*/") and in_comment is True:
                    in_comment = False
                    ended_comment = True
                elif ended_comment is True and line.strip() != str():
                    entry[1] += self.clean(line)
                    if line.strip().endswith(";") or line.strip().endswith('{'):
                        ended_comment = False
                        entry.append(scope[:])
                        entry.append(Typenames.get_type(entry[1]))
                        self.data.append(entry)
                elif ended_comment is True:
                    ended_comment = False
                    entry.append(scope[:])
                    entry.append(Typenames.get_type(entry[1]))
                    self.data.append(entry)
                elif ended_comment is False:
                    if Typenames.get_type(line) is not Typenames.NONE:
                        self.data.append([[],
                                          self.clean(line), scope[:],
                                          Typenames.get_type(line)])
                if line.strip().endswith("{"):
                    scope.append(self.clean(line))
                if line.strip().startswith("}"):
                    scope.pop()
        pprint(self.data)

    def read_function(self, line):
        line = line.strip()
        if re.compile("([^\s]*)\s?([^\s()]+)\((.*)\)(;|(\s*{))").match(
                line) is not None:
            return True
        else:
            return False

    def clean(self, line):
        newline = False
        line = line.strip()
        if line.startswith("* "):
            line = line[2:]
        elif line.startswith("/**"):
            line = line[3:]
        elif line.startswith("/*!"):
            line = line[3:]
        elif line.startswith("*/"):
            line = line[2:]
        elif line.startswith("*"):
            line = line[1:]
        if line.endswith("*/"):
            line = line[:-2]
        if line.endswith(" {"):
            line = line[:-2]
        if line.endswith("{"):
            line = line[:-1]
        if line.endswith(";"):
            line = line[:-1]
        if line == str():
            return None
        return line
