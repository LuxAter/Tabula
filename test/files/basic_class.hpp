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

/**
 * @file template.hpp
 * @brief This is a test file for C++ parsing
 * @author Arden Rasmussen
 * @version 0.0
 * @date 2017-10-22
 */

#ifndef EXAMPLES_TEMPLATE_HPP_
#define EXAMPLES_TEMPLATE_HPP_

static unsigned tmp = 15;

/**
 * @brief Test namespace
 */
namespace test {

  /**
   * @brief This is a test enum
   */
  enum TestEnum {
    TEST_A = 0,  //!< A value
    TEST_B = 1   //!< B value
  };

  /**
   * @brief Will return false. And now it is also a test as to what will happen
   * to a long definition, and paragraph splitting.
   *
   * @tparam _A First type
   * @tparam _B Second Type
   * @param lhs first value of `_A`
   * @param rhs second value of `_B` This is an especially long comment block.
   *        Lets see if it will work.
   *
   * @return `false`
   */
  template <typename _A, typename _B>
  bool same(_A lhs, _B rhs, int mhs) {
    return false;
  }

  int add(int a, int b);

  /**
   * @brief Template class for scope testing
   */
  class Template {
    static int val;
    /**
     * @brief test function in tempalte class
     *
     * @param b var b
     *
     * @return returns b
     */
    double testing(int b) const { return b; }
  };

}  // namespace test

int sum(int a, int b);

#endif  // EXAMPLES_TEMPLATE_HPP_
