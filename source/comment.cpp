#include "comment.hpp"

#include <string>
#include <vector>

void tabula::Comment::ParseComment(std::string str) {
  std::vector<std::string> lines;
  std::string tmp;
  for (size_t i = 0; i < str.size(); i++) {
    if (str[i] == '\n') {
      for (size_t j = 0; j < tmp.size() && tmp[j] == ' '; j++) {
        tmp.erase(tmp.begin());
        j--;
      }
      if (tmp.substr(0, 3) == "/**") {
        tmp.erase(tmp.begin(), tmp.begin() + 3);
      } else if (tmp.substr(0, 2) == "* ") {
        tmp.erase(tmp.begin(), tmp.begin() + 1);
      } else if (tmp.substr(0, 1) == "*") {
        tmp.erase(tmp.begin());
      } else if (tmp.substr(0, 2) == "*/") {
        tmp.erase(tmp.begin(), tmp.begin() + 1);
      }
      raw_comment += tmp + '\n';
      lines.push_back(tmp);
      tmp = std::string();
    } else {
      tmp += str[i];
    }
  }
}

std::string tabula::Comment::GetRawComment() { return raw_comment; }
