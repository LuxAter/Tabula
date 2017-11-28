from pprint import pprint
import data.commands
import sys
import markdown

class Entry:
    def __init__(self):
        self.name = str()
        self.sub_entries = list()
        self.source = list()
        self.raw_comment = str()
        self.doc = dict()
        self.source_file = str()
        self.kind = str()

    def __repr__(self):
        return "{{\n 'name': \"{}\",\n 'source_file': \"{}\",\n 'source': {},\n 'doc': {},\n 'raw_comment': \"{}\",\n 'sub_entries': {}\n}}".format(self.name, self.source_file, self.source, self.doc, repr(self.raw_comment), self.sub_entries)

    def string(self, indent=0):
        i = ' ' * indent
        string = str()
        string += i + "'name': \'{}\',\n".format(self.name)
        string += i + "'source_file': \'{}\',\n".format(self.source_file)
        string += i + "'source': {},\n".format(self.source)
        string += i + "'doc': {},\n".format(self.doc)
        string += i + "'raw_comment': \'{}\',\n".format(self.raw_comment)
        string += i + "'sub_entires': \n"
        for sub in self.sub_entries:
            string += sub.string(indent + 2)
        return string


    def parse_command(self, line):
        specific = False
        if line.startswith(('@', '\\', ':')) is False:
            raise ValueError('Command does not begin with indicator')
        if line[0] == ':':
            specific = True
        line = line[1:]
        data.commands.open_commands()
        words = line.split()
        if len(words) == 0:
            raise ValueError('Line is blank after indicator')
        if specific is True and words[0].endswith(':'):
            words[0] = words[0][:-1]
            closed = True
        elif specific is True:
            closed = False
        if words[0] not in data.commands.commands:
            raise ValueError('Unrecognized command', words[0])
        cmd = data.commands.commands[words[0]]
        index = words[0]
        if index not in self.doc:
            self.doc[index] = list()
        if specific is False:
            ent = dict()
            ent['attr'] = words[1:cmd[0] + 1]
            ent['content'] = ' '.join(words[cmd[0]+1:])
            self.doc[index].append(ent)
        else:
            ent = dict()
            ent['attr'] = list()
            args = 1
            if closed is False:
                for word in words[1:cmd[2]+1]:
                    args += 1
                    if word.endswith(':'):
                        ent['attr'] .append(word[:-1])
                        break
                    else:
                        ent['attr'].append(word)
            ent['content'] = ' '.join(words[args:])
            self.doc[index].append(ent)

    def parse_comment(self):
        lines = self.raw_comment.split('\n')
        data.commands.open_commands()
        paragraphs = list()
        self.doc['content'] = str()
        in_command = False
        for line in lines:
            if line.startswith(('@', '\\', ':')):
                paragraphs.append(line)
                in_command = True
            elif line == str():
                if in_command is True:
                    in_command = False
                paragraphs.append(str())
            elif in_command is True:
                paragraphs[-1] += ' ' + line.strip()
            elif in_command is False:
                paragraphs.append(line)
        for par in paragraphs:
            par = par.strip()
            if len(par.split()) > 0 and data.commands.is_command(par.split()[0]) is True:
                self.parse_command(par)
            elif par == str():
                self.doc['content'] += '\n'
            else:
                self.doc['content'] += par + '\n'
        html = markdown.markdown(self.doc['content'], extensions=['markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.codehilite'])

