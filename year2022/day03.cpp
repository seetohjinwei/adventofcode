#include "definitions.h"
#include "parser.h"
#include <fstream>
#include <iostream>
#include <unordered_set>

using namespace std;

int getPriority(char c) {
  if ('a' <= c && c <= 'z') {
    return c - 'a' + 1;
  } else {
    return c - 'A' + 27;
  }
}

ll part1() {
  ifstream data {"day03.in"};

  ll result = 0;

  int len, i;
  string s;
  while (data >> s) {
    len = s.size();

    unordered_set<char> seen {};
    for (i = 0; i < len / 2; i++) {
      seen.insert(s[i]);
    }
    for (i = len / 2; i < len; i++) {
      if (seen.find(s[i]) != seen.end()) {
        result += getPriority(s[i]);
        break;
      }
    }
  }

  return result;
}

ll part2() {
  ifstream data {"day03.in"};

  ll result = 0;

  string s1, s2, s3;
  while (data >> s1 >> s2 >> s3) {
    unordered_set<char> seen1, seen2;

    for (const auto& c : s1)
      seen1.insert(c);
    for (const auto& c : s2)
      seen2.insert(c);
    for (const auto& c : s3)
      if (seen1.find(c) != seen1.end() && seen2.find(c) != seen2.end()) {
        result += getPriority(c);
        break;
      }
  }

  return result;
}

int main() {
  cout << "part1: " << part1() << '\n';
  cout << "part2: " << part2() << '\n';
  return 0;
}
