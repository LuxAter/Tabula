from data.entry import Entry

class HtmlGenerator:
    def __init__(self):
        self.multi_file = True
        self.templates = dict()
        self.dest_path = str()
