from enum import Enum

class Type(Enum):
    NONE = 0
    PAGE = 1
    PARAGRAPH = 2
    FUNCTION = 3
    PARAM = 4
    RETURN = 5

class Block(object):

    def __init__(self):
        self.data = list()
        self.metadata = list()
        self.type = Type.NONE

    def __repr__(self):
        return repr(self.type) + repr(self.metadata) + ':' + repr(self.data)

    def set_type(self, tp):
        if isinstance(tp, str):
            if tp == 'page':
                self.type = Type.PAGE
            elif tp == 'par':
                self.type = Type.PARAGRAPH
            elif tp == 'func':
                self.type = Type.FUNCTION
            elif tp == 'param':
                self.type = Type.PARAM
            elif tp == 'return':
                self.type = Type.RETURN
            pass
        else:
            self.type = tp

    def set_meta(self, line):
        self.set_type(line.split()[0][1:])
        if self.type is Type.FUNCTION:
            self.metadata = [' '.join(line.split()[1:])]
        else:
            self.metadata = line.split()[1:]

    def append(self, obj):
        if isinstance(obj, str) and obj == str():
            return
        elif isinstance(obj, str) and self.data and isinstance(self.data[-1], str):
            self.data[-1] += '\n' + obj
        else:
            self.data.append(obj)
