from tabula.parser import Parser
from tabula.generator import Generator

def main():
    my_parse = Parser('.')
    my_generator = Generator('../tabula/templates/texinfo.texi')
    data = my_parse.parse()
    result = my_generator.generate(data)

    # print(result)

if __name__ == "__main__":
    main()
