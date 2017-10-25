#include <clang-c/Index.h>
#include <iostream>

std::ostream& operator<<(std::ostream& stream, const CXString& str) {
  stream << clang_getCString(str);
  clang_disposeString(str);
  return stream;
}

int main(int argc, char const* argv[]) {
  CXIndex index = clang_createIndex(0, 0);
  CXTranslationUnit unit =
      clang_parseTranslationUnit(index, "test/files/basic_class.hpp", nullptr,
                                 0, nullptr, 0, CXTranslationUnit_None);
  if (unit == nullptr) {
    std::cerr << "Unable to parse translation unit, Quitting." << std::endl;
    exit(-1);
  }
  CXCursor cursor = clang_getTranslationUnitCursor(unit);
  clang_visitChildren(
      cursor,
      [](CXCursor c, CXCursor parent, CXClientData client_data) {
        std::cout << "Cursor \'" << clang_getCursorSpelling(c)
                  << "\' of kind \'"
                  << clang_getCursorKindSpelling(clang_getCursorKind(c))
                  << "\'\n";
        // CXString com = clang_Cursor_getRawCommentText(c);
        // std::cout << "Comment: \"" << com << "\"\n";
        // std::cout << "Comment: \"" << clang_FullComment_getAsHTML(com);
        if (clang_Location_isInSystemHeader(clang_getCursorLocation(c)) != 0) {
          return CXChildVisit_Continue;
        }
        return CXChildVisit_Recurse;
      },
      nullptr);
  clang_disposeTranslationUnit(unit);
  clang_disposeIndex(index);
  return 0;
}
