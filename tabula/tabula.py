#!/usr/bin/python3

from parsers.cpp.parser import CppParser


def main():
    parser = CppParser()
    parser.read("../examples/template.hpp")


if __name__ == "__main__":
    main()
