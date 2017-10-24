"""C++ Documented types"""

import re
from enum import Enum


class Typenames(Enum):
    NONE = 0
    NAMESPACE = 1
    CLASS = 2
    STRUCT = 3
    FUNCTION = 4
    ENUM = 5
    FILE = 6

    @staticmethod
    def get_type(line):
        line = line.strip()
        regex = list()
        regex.append([re.compile("namespace [^\s{]+"), Typenames.NAMESPACE])
        regex.append([re.compile("class [^\s{]+"), Typenames.CLASS])
        regex.append([re.compile("struct [^\s{]+"), Typenames.STRUCT])
        regex.append([
            re.compile("([^\s]*)\s?([^\s()]+)\((.*)\)(;|(\s*{))"),
            Typenames.FUNCTION
        ])
        regex.append([
            re.compile("template\s?<[^>]+>\s?([^\s]*)\s?([^\s()]+)\((.*)\)"),
            Typenames.FUNCTION
        ])
        regex.append([re.compile("enum [^\s{]+"), Typenames.ENUM])
        for match in regex:
            if match[0].match(line) is not None:
                return match[1]
        return Typenames.NONE
