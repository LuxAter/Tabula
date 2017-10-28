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

#ifndef TABULA_DATA_HPP_
#define TABULA_DATA_HPP_

#include <array>
#include <map>
#include <string>
#include <utility>
#include <vector>

#include "clang-c/Index.h"
#include "code.hpp"

namespace tabula {

  struct Entity {
    std::string str, type_str, kind_str, comment_str, scope_str;
    unsigned int kind;
    CXType type;
    std::array<unsigned, 5> info;
    std::vector<std::pair<unsigned int, std::string> > scope;
  };

  extern std::vector<Entity> entries;

  enum NoteType {
    FATAL_ERROR = 1,
    ERROR = 2,
    WARNING = 3,
    INFO = 4,
    SUCCESS = 6,
    GOOD = 7,
    SECTION = 8
  };

  void Notification(NoteType type, std::string str, Entity entry,
                    bool output = true, bool color = true);
  void Notification(NoteType type, std::string str, bool output = true,
                    bool color = true);

  void UncommentedWarning(bool color = false);
  void RemoveUncommented(bool output = true, bool color = false);
  void ParseComment(std::vector<Entity>::iterator entity);
  void ParseComments(bool output = true, bool color = false);
  void ParseFile(std::string file_path, bool output = true, bool color = false);
}  // namespace tabula

#endif  // TABULA_DATA_HPP_
