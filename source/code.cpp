#include "code.hpp"

#include <map>
#include <string>
#include <vector>

std::string tabula::GetLanguageString(unsigned int language) {
  std::map<unsigned int, std::string> lang_str;
  lang_str[Language::NONE] = "(NONE)";
  lang_str[Language::CPP] = "C++";
  lang_str[Language::PYTHON] = "Python";
  return lang_str[language];
}

tabula::CodeBlock::CodeBlock() : language(Language::NONE) {}

tabula::CodeBlock::CodeBlock(std::string code, Language lang)
    : language(lang), code_block(code) {}

tabula::CodeBlock::~CodeBlock() { language = Language::NONE; }

void tabula::CodeBlock::SetCode(std::string code) { code_block = code; }

void tabula::CodeBlock::SetLanguage(Language lang) { language = lang; }

std::string tabula::CodeBlock::GetCode() { return code_block; }

tabula::Language tabula::CodeBlock::GetLanguage() { return language; }
