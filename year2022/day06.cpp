#include "definitions.h"
#include "parser.h"
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

inline int get_index(char c) {
  return c - 'a';
}

int crunch(string s, int num) {
  int counter[26], unique = 0;
  fill(begin(counter), end(counter), 0);

  for (int i = 0; i < num; i++) {
    if (counter[get_index(s[i])]++ == 0)
      unique++;
  }
  for (int i = num; i < s.size(); i++) {
    if (unique == num) {
      return i;
    }

    if (--counter[get_index(s[i - num])] == 0)
      unique--;
    if (counter[get_index(s[i])]++ == 0)
      unique++;
  }

  return s.size();
}

int main() {
  ifstream data("day06.in");
  string s;
  data >> s;

  cout << "part1: " << crunch(s, 4) << endl;
  cout << "part2: " << crunch(s, 14) << endl;

  return 0;
}
