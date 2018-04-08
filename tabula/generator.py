from tabula.block import Type, Block
from tabula.text import Format, Text

class Generator(object):
    def __init__(self, path):
        self.template_file = path
        self.templates = dict()
        self.load_templates()

    def convert_key(self, key):
        for tp in Type:
            if repr(tp).split()[0][6:-1].lower() == key.lower():
                return tp
        for fmt in Format:
            if repr(fmt).split()[0][8:-1].lower() == key.lower():
                return fmt
        return None


    def load_templates(self):
        with open(self.template_file, 'r') as file:
            lines = file.read().splitlines()
        key = str()
        value = str()
        for line in lines:
            if line.startswith('[[') and line.endswith(']]'):
                if key:
                    self.templates[self.convert_key(key)] = value[:-1]
                key = line[2:-2]
                value = str()
            else:
                value += line + '\n'
        if key:
            self.templates[self.convert_key(key)] = value[:-1]

    def generate(self, block):
        if block.type in self.templates:
            template = self.templates[block.type]
        else:
            print("Unknown block: {}".format(repr(block.type)))
            template = self.templates[Format.TEXT]
        data = {Format.TEXT: str()}
        for entry in block.data:
            if isinstance(entry, str):
                data[Format.TEXT] += entry
            elif isinstance(entry, Text):
                data[Format.TEXT] += self.generate(entry)
            else:
                if entry.type in data:
                    data[entry.type] += '\n' + self.generate(entry)
                else:
                    data[entry.type] = self.generate(entry)
        template = template.replace('$?', data[Format.TEXT])
        for i, meta in enumerate(block.metadata):
            template = template.replace('$' + repr(i + 1), meta)
        for key in data:
            template = template.replace('$' + repr(key).split('.')[1].split()[0][:-1].lower(), data[key])
        return template

