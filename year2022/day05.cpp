#include "definitions.h"
#include "parser.h"
#include <fstream>
#include <iostream>
#include <regex>
#include <stack>
#include <vector>

using namespace std;

struct result {
  string _stack;
  string _vector;
};

result crunch() {
  ifstream data("day05.in");

  vector<vector<char>> vectors;

  // parsing crates
  string line;
  int i, stack_i;
  char c;
  bool found;
  while (getline(data, line)) {
    found = false;
    // 1, 5, 9, 13, ...
    for (i = 1; i < line.size(); i += 4) {
      c = line[i];
      if (c < 'A' || c > 'Z') {
        continue;
      }
      found = true;
      stack_i = i / 4;
      while (stack_i >= vectors.size()) {
        vector<char> new_stack;
        vectors.pb(new_stack);
      }
      vectors.at(stack_i).pb(c);
    }

    // don't steal the remaining lines
    if (!found)
      break;
  }

  vector<stack<char>> stacks;
  for (auto& v : vectors) {
    stack<char> s;
    for (auto it = v.end() - 1; it >= v.begin(); it--) {
      s.push(*it);
    }
    stacks.pb(s);
  }

  // here, `stacks` is ready

  for (auto &v : vectors) {
    reverse(v.begin(), v.end());
  }

  // here, `vectors` is ready

  string _;
  int amount, from, to;
  while (data >> _ >> amount >> _ >> from >> _ >> to) {
    // simulate vector
    vector<char> &f = vectors.at(from - 1);
    vector<char> &t = vectors.at(to - 1);
    for (auto it = f.end() - amount; it < f.end(); it++) {
      t.pb(*it);
    }

    f.erase(f.end() - amount, f.end());

    // simulate stack
    while (amount-- > 0) {
      stack<char> &f = stacks.at(from - 1);
      stack<char> &t = stacks.at(to - 1);
      c = f.top(); f.pop();
      t.push(c);
    }
  }

  // collate _stack
  string _stack;
  for (auto& s : stacks) {
    _stack += s.top();
  }

  string _vector;
  for (auto& v : vectors) {
    _vector += v.back();
  }

  return { _stack, _vector };
}

int main() {
  result res = crunch();
  cout << "part1: " << res._stack << '\n';
  cout << "part2: " << res._vector << '\n';

  return 0;
}
