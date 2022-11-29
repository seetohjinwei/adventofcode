#include "parser.h"
#include <fstream>
#include <string>
#include <vector>

using namespace std;

/**
 * Reads a file into lines.
 *
 * Adapted from https://stackoverflow.com/a/51572325
 */
vector<string> readFile(const string& fileName) {
  vector<string> result {};

  ifstream file(fileName);
  if (file.is_open()) {
    string line;
    while (getline(file, line)) {
      string ss = line.c_str();
      result.push_back(ss);
    }
  }
  file.close();

  return result;
}

/**
 * Splits a string by a delimiter.
 *
 * Adapted from https://stackoverflow.com/a/14267455
 */
vector<string> split(const string& s, const string& delimiter) {
  vector<string> result {};
  int dl = delimiter.length();

  size_t lo = 0;
  size_t hi = s.find(delimiter);
  while (hi != string::npos) {
    string ss = s.substr(lo, hi - lo);
    result.push_back(ss);
    lo = hi + dl;
    hi = s.find(delimiter, lo);
  }
  string ss = s.substr(lo, hi);
  result.push_back(ss);

  return result;
}
