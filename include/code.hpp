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

#ifndef TABULA_CODE_HPP_
#define TABULA_CODE_HPP_

#include <string>
#include <vector>

namespace tabula {
  enum Language { NONE = 0, CPP = 1, PYTHON = 2 };
  std::string GetLanguageString(unsigned int language);
  class CodeBlock {
   public:
    CodeBlock();
    CodeBlock(std::string code, Language lang);
    ~CodeBlock();

    void SetCode(std::string code);
    void SetLanguage(Language lang);

    std::string GetCode();
    Language GetLanguage();

   private:
    Language language;
    std::string code_block;
  };
}  // namespace tabula

#endif  // TABULA_CODE_HPP_
