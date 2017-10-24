#!/usr/bin/python3

from parsers.cpp.parser import CppParser


def main():
    parser = CppParser()
    parser.read("../examples/template.hpp")
    #  print(parser.generate_entity())


if __name__ == "__main__":
    main()
