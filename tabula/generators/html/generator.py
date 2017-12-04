import markdown
import collections
from data.entry import Entry
from jinja2 import Environment, PackageLoader


class HtmlGenerator:

    def __init__(self, entry=Entry()):
        self.multi_file = True
        self.templates = dict()
        self.dest_path = str()
        self.tree = entry
        self.enviormant = Environment(loader=PackageLoader('tabula', 'templates'))

    def generate_html(self, text):
        text = markdown.markdown(
            text,
            extensions=[
                'markdown.extensions.extra', 'markdown.extensions.admonition',
                'markdown.extensions.codehilite'
            ])
        if text.count('<p>') == 1:
            text = text[3:-4]
        return text

    def path_to_string(self, entry):
        if isinstance(entry, dict):
            for value in entry.items():
                if isinstance(value[1], str):
                    entry[value[0]] = self.generate_html(value[1])
                else:
                    entry[value[0]] = self.path_to_string(value[1])
        elif isinstance(entry, list):
            for i, value in enumerate(entry):
                if isinstance(value, str):
                    entry[i] = self.generate_html(value)
                else:
                    entry[i] = self.path_to_string(value)
        return entry

    def compile_entry(self, entry):
        self.path_to_string(entry.doc)
        for key, value in entry.sub_entries.items():
            for ent in value:
                self.compile_entry(ent)

    def compile_entry_tree(self):
        self.compile_entry(self.tree)

    def generate_entry_html(self):
        return ""
