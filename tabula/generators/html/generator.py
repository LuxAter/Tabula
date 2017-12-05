import markdown
import collections
from data.entry import Entry
from jinja2 import Environment, PackageLoader
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


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

    def generate_code(self, code, lang):
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter(linenos=False, cssclass="source")
        result = highlight(code, lexer, formatter)
        return result

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
        for i in range(2, len(entry.source)):
            entry.source[i] = self.generate_code(entry.source[i], entry.source[0])
        for key, value in entry.sub_entries.items():
            for ent in value:
                self.compile_entry(ent)

    def compile_entry_tree(self):
        self.compile_entry(self.tree)

    def generate_entry_html(self, group, ent):
        template = self.enviormant.get_template("html/" + group.lower() + ".html")
        return template.render(obj=ent)

    def generate_tree_html(self):
        result = str()
        for group, value in self.tree.sub_entries.items():
            for child in value:
                result += self.generate_entry_html(group, child)
        return result
