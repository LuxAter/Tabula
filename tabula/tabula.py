#!/usr/bin/python3

from data import entry
from parsers.cpp.parser import CppParser
#  from parsers.cpp.parser import CppParser

def visit(parent, indent):
    #  print(indent, ">>>", parent.spelling)
    #  print(indent, "   Comment:\n   ", parent.raw_comment)
    for child in parent.get_children():
        visit(child, indent + " ")

def main():
    parser = CppParser()
    tu = parser.get_trans_unit("../examples/template.hpp")
    doc = parser.generate_tree(tu)
    print(doc.string())

    #  from clang import cindex
    #  lname = "/usr/lib/llvm-5.0/lib/libclang.so"
    #  cindex.Config.set_library_file(lname)
    #  index = cindex.Index.create()
    #  tu = index.parse("../examples/template.hpp")
    #  if not tu:
        #  print("unable to load input", stdout=sys.stderr)
    #  visit(tu.cursor, "")
    #  obj = entry.Entry()
    #  obj.raw_comment ="""@brief Will return false

#  This is a test function that uses templates and other stuf! I am adding more
#  stuff to this documentation to see if the paragraphs are generated correctly.

#  @tparam _A First type
#  @tparam _B Second Type
#  :param lhs _A [in]: first value of `_A`
#  !!! note "Testings"
    #  THis is a testing note!!!
    #  this is more of this paragraph...

#  !!! warning "This is a warning"

#  ```c++
#  #include <iostream>

#  void main(int argc, const char** argv){
    #  return 0;
#  }
#  ```
#  @param rhs second value of `_B` This is an especially long comment block.
       #  Lets see if it will work.

#  @return `false`"""
    #  obj.parse_comment()
    #  print(curs)
    #  if not tu:
        #  parser.error("unable to load input")

    #  # A helper function for generating the node name.
    #  def name(f):
        #  if f:
            #  return "\"" + f.name + "\""

    #  # Generate the include graph
    #  out.write("digraph G {\n")
    #  for i in tu.get_includes():
        #  line = "  ";
        #  if i.is_input_file:
            #  # Always write the input file as a node just in case it doesn't
            #  # actually include anything. This would generate a 1 node graph.
            #  line += name(i.include)
        #  else:
            #  line += '%s->%s' % (name(i.source), name(i.include))
        #  line += "\n";
        #  out.write(line)
    #  out.write("}\n")
    #  parser = CppParser()
    #  parser.read("../examples/template.hpp")
    #  print(parser.generate_entity())


if __name__ == "__main__":
    main()
