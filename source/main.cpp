// #include <clang-c/Index.h>
#include <iostream>
#include <vector>

#include "cpp_parser.hpp"
#include "data.hpp"

int main(int argc, char const* argv[]) {
  tabula::ParseFile("test/files/basic_class.hpp", true, true);
  tabula::ParseFile("test/files/basic_class", true, true);
  tabula::UncommentedWarning(true);
  tabula::RemoveUncommented(true, true);
  tabula::ParseComments(true, true);
  for (int i = 0; i < tabula::entries.size(); i++) {
    std::cout << tabula::entries[i].scope_str << "::" << tabula::entries[i].str
              << "\n";
  }
  return 0;
}
