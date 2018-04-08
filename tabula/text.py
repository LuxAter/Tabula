from enum import Enum

class Format(Enum):
    NONE = 0
    TEXT = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    MATH = 5
    REF = 6

class Text(object):

    def __init__(self):
        self.data = list()
        self.metadata = list()
        self.type = Format.NONE

    def __repr__(self):
        return repr(self.type) + repr(self.metadata) + ':' + repr(self.data)

    def append(self, obj):
        self.data.append(obj)

    def cat(self, obj):
        self.data += obj.data

