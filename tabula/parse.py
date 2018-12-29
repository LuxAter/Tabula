import tabula.message as msg

def parse_doc(src):
    if src and src[0] == '':
        src = src[1:]
    return src

def parse_enum(src, line):
    return line + 2, {'type': 'enum', 'src': "SOURCE"}

def parse_ref(src):
    if src and src[0] == '':
        src = src[1:]
    line = 0
    ref = []
    types = ["<!-- {} -->".format(x) for x in ("func", "enum", "par", "struct", "class")]
    def find_next(line):
        while line < len(src) and src[line] not in types:
            line += 1
        return line
    while line < len(src):
        line = find_next(line)
        if line >= len(src):
            return ref
        if src[line] == "<!-- func -->":
            line += 1
        elif src[line] == "<!-- enum -->":
            line, doc = parse_enum(src, line)
            ref.append(doc)
    return ref

def parse(file, src):
    if not src:
        msg.warning("File \"{}\" is empty".format(file))
        return {}
    if src[0] == "<!-- doc -->":
        return {"type": "doc", "src": parse_doc(src[1:])}
    elif src[0] == "<!-- ref -->":
        return {"type": "ref", "src": parse_ref(src[1:])}
    return {}

def parse_file(file):
    with open(file) as f:
        return parse(file, [x.rstrip() for x in f.readlines()])
    return []
