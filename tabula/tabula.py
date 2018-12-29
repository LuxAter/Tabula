from pprint import pprint
import glob
import yaml
import tabula.message as msg
import tabula.parse as parse

def main():
    config = {}
    with open('tabula.yml', 'r') as file:
        config = yaml.load(file)
    if 'source' not in config:
        config['source'] = 'source'
    if 'dest' not in config:
        config['dest'] = 'build'
    pprint(config)
    files = list(glob.iglob(config['source'] + '/**/*.md', recursive=True))
    for file in files:
        print(file)
        tree = parse.parse_file(file)
        print(tree)

