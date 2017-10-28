#include "cpp_parser.hpp"

#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "clang-c/Documentation.h"
#include "clang-c/Index.h"
#include "code.hpp"
#include "data.hpp"

std::vector<std::map<std::string, std::string>> tabula::cpp::ParseFile(
    std::string file_path) {
  CXIndex index = clang_createIndex(0, 0);
  CXTranslationUnit unit = clang_parseTranslationUnit(
      index, file_path.c_str(), nullptr, 0, nullptr, 0, CXTranslationUnit_None);
  if (unit == nullptr) {
    std::cerr << "Unable to parse translation unit, Quitting." << std::endl;
    exit(-1);
  }
  CXCursor cursor = clang_getTranslationUnitCursor(unit);
  Entity entry;
  entry.str = GetString(clang_getCursorSpelling(cursor));
  entry.type_str =
      GetString(clang_getTypeSpelling(clang_getCursorType(cursor)));
  entry.kind_str =
      GetString(clang_getCursorKindSpelling(clang_getCursorKind(cursor)));
  entry.comment_str = GetString(clang_Cursor_getRawCommentText(cursor));
  entry.scope_str = GetScopeStr(GetScope(cursor));
  entry.type = clang_getCursorType(cursor);
  entry.kind = clang_getCursorKind(cursor);
  entry.info = FunctionDeclInfo(cursor);
  entry.scope = GetString(GetScope(cursor));
  entries.push_back(entry);
  clang_visitChildren(cursor, tabula::cpp::VisitChildren, nullptr);
  clang_disposeTranslationUnit(unit);
  clang_disposeIndex(index);
  return std::vector<std::map<std::string, std::string>>();
}

CXChildVisitResult tabula::cpp::VisitChildren(CXCursor cursor, CXCursor parent,
                                              CXClientData data) {
  Entity entry;
  entry.str = GetString(clang_getCursorSpelling(cursor));
  entry.type_str =
      GetString(clang_getTypeSpelling(clang_getCursorType(cursor)));
  entry.kind_str =
      GetString(clang_getCursorKindSpelling(clang_getCursorKind(cursor)));
  entry.comment_str = GetString(clang_Cursor_getRawCommentText(cursor));
  entry.scope_str = GetScopeStr(GetScope(cursor));
  entry.type = clang_getCursorType(cursor);
  entry.kind = clang_getCursorKind(cursor);
  entry.info = FunctionDeclInfo(cursor);
  entry.scope = GetString(GetScope(cursor));
  entries.push_back(entry);
  unsigned kind = clang_getCursorKind(cursor);
  if (kind == 22 || kind == 4 || kind == 5) {
    return CXChildVisit_Recurse;
  }
  return CXChildVisit_Continue;
}

std::array<unsigned, 5> tabula::cpp::FunctionDeclInfo(CXCursor cursor) {
  return std::array<unsigned, 5>{
      {clang_CXXMethod_isConst(cursor), clang_CXXMethod_isStatic(cursor),
       clang_CXXMethod_isVirtual(cursor), clang_CXXMethod_isDefaulted(cursor),
       clang_CXXMethod_isPureVirtual(cursor)}};
}

std::vector<std::pair<CXCursorKind, CXString>> tabula::cpp::GetScope(
    CXCursor cursor) {
  CXCursor parent = cursor;
  std::vector<std::pair<CXCursorKind, CXString>> scope;
  while (clang_isTranslationUnit(clang_getCursorKind(parent)) == 0) {
    parent = clang_getCursorSemanticParent(parent);
    scope.insert(scope.begin(), std::pair<CXCursorKind, CXString>(
                                    clang_getCursorKind(parent),
                                    clang_getCursorSpelling(parent)));
  }
  return scope;
}

std::string tabula::cpp::GetScopeStr(
    std::vector<std::pair<CXCursorKind, CXString>> scope) {
  std::string scope_str = "";
  for (int i = 0; i < scope.size(); i++) {
    scope_str += GetString(scope[i].second);
    if (i != scope.size() - 1) {
      scope_str += "::";
    }
  }
  return scope_str;
}

std::string tabula::cpp::GetString(CXString cx_str) {
  if (clang_getCString(cx_str) == nullptr) {
    return std::string();
  }
  std::string str(clang_getCString(cx_str));
  clang_disposeString(cx_str);
  return str;
}

std::vector<std::pair<unsigned int, std::string>> tabula::cpp::GetString(
    std::vector<std::pair<CXCursorKind, CXString>> scope) {
  std::vector<std::pair<unsigned int, std::string>> ret;
  for (int i = 0; i < scope.size(); i++) {
    ret.push_back(std::pair<unsigned int, std::string>(
        scope[i].first, GetString(scope[i].second)));
  }
  return ret;
}
