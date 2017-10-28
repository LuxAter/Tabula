#include "data.hpp"

#include <iomanip>
#include <iostream>

#include "cpp_parser.hpp"

namespace tabula {
  std::vector<Entity> entries;
}  // namespace tabula

void tabula::Notification(NoteType type, std::string str, Entity entry,
                          bool output, bool color) {
  std::string scope = entry.scope_str;
  if (scope != std::string()) {
    scope += "::";
  }
  scope += entry.str;
  Notification(type, str + " \"" + scope + "\"", output, color);
}
void tabula::Notification(NoteType type, std::string str, bool output,
                          bool color) {
  if (output == false) {
    return;
  }
  std::map<NoteType, std::string> repr{
      {FATAL_ERROR, "FATAL  "}, {ERROR, "ERROR  "},   {WARNING, "WARNING"},
      {INFO, "INFO   "},        {SUCCESS, "SUCCESS"}, {GOOD, "GOOD   "},
      {SECTION, "SECTION"}};
  if (color == true) {
    if (type == FATAL_ERROR) {
      std::cout << "\033[1;31m";
    } else if (type == ERROR) {
      std::cout << "\033[31m";
    } else if (type == WARNING) {
      std::cout << "\033[93m";
    } else if (type == INFO) {
      std::cout << "\033[97m";
    } else if (type == SUCCESS) {
      std::cout << "\033[32m";
    } else if (type == GOOD) {
      std::cout << "\033[32m";
    } else if (type == SECTION) {
      std::cout << "\033[1;97m";
    }
  }
  std::cout << "[ " << repr[type] << " ] " << str << "\n";
  if (color == true) {
    std::cout << "\033[0m";
  }
}

void tabula::UncommentedWarning(bool color) {
  for (int i = 0; i < entries.size(); i++) {
    if (entries[i].comment_str == std::string()) {
      Notification(WARNING, "Entity is uncommented", entries[i], true, color);
    }
  }
}

void tabula::RemoveUncommented(bool output, bool color) {
  for (std::vector<Entity>::iterator it = entries.begin(); it != entries.end();
       ++it) {
    if (it->comment_str == std::string()) {
      Notification(INFO, "Removing Uncommented Entry", *it, output, color);
      entries.erase(it);
      --it;
    }
  }
}

void tabula::ParseComments(bool output, bool color) {
  for (std::vector<Entity>::iterator it = entries.begin(); it != entries.end();
       ++it) {
    // ParseComment(it);
    Notification(SUCCESS, "Parsed Entry Comment", *it, output, color);
  }
}

void tabula::ParseFile(std::string file_path, bool output, bool color) {
  std::string ext = file_path.substr(file_path.find_last_of(".") + 1);
  if (ext == "hpp" || ext == "cpp" || ext == "cxx" || ext == "hxx") {
    Notification(SECTION, "Parsing \"" + file_path + "\" as C++ File", output,
                 color);
    tabula::cpp::ParseFile(file_path);

  } else if (ext == "py") {
    Notification(ERROR, "Python Files Are Not Yet Supported", output, color);
    // Notification(SECTION, "Parsing \"" + file_path + "\" as Pythton File",
    // output, color);
  } else {
    Notification(FATAL_ERROR, "Unknown File Extension \"" + ext + "\"", output,
                 color);
  }
}
