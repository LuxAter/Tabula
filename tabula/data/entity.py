from pprint import pformat, pprint


class Entity:

    def __init__(self, entity_type=None):
        self.typename = entity_type
        self.comments = list()
        self.scope = list()
        self.code = str()
        self.sub_entity = list()

    def __repr__(self):
        return pformat(self.typename) + '\n' + pformat(
            self.comments) + '\n' + pformat(self.sub_entity)

    def parse_comment(self, comment):
        prev_indent = None
        for line in comment:
            print(prev_indent, len(line) - len(line.lstrip()))
            if prev_indent is None:
                self.comments.append(line)
                prev_indent = len(line.split()[0]) + 1
            elif prev_indent == len(line) - len(line.lstrip()):
                self.comments[-1] += ' ' + line.lstrip()
            else:
                self.comments.append(line)
                prev_indent = len(line.split()[0]) + 1

    def parse_scope(self, scope):
        self.scope = scope

    def parse_code(self, code):
        self.code = code
