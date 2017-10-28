/* Copyright (C)
 * 2017 - Arden Rasmussen
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 *
 */

#ifndef TABULA_CPP_PARSER_HPP_
#define TABULA_CPP_PARSER_HPP_

#include <array>
#include <map>
#include <string>
#include <vector>

#include "clang-c/Index.h"

namespace tabula {
  namespace cpp {
    std::vector<std::map<std::string, std::string>> ParseFile(
        std::string file_path);

    CXChildVisitResult VisitChildren(CXCursor cursor, CXCursor parent,
                                     CXClientData data);
    std::array<unsigned, 5> FunctionDeclInfo(CXCursor cursor);
    std::vector<std::pair<CXCursorKind, CXString>> GetScope(CXCursor cursor);
    std::string GetScopeStr(
        std::vector<std::pair<CXCursorKind, CXString>> scope);
    std::string GetString(CXString cx_str);
    std::vector<std::pair<unsigned int, std::string>> GetString(
        std::vector<std::pair<CXCursorKind, CXString>> scope);
  }  // namespace cpp
}  // namespace tabula

#endif  // TABULA_CPP_PARSER_HPP_
