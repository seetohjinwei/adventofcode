#include "definitions.h"
#include "parser.h"
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

struct result {
  int full;
  int partial;
};

result crunch() {
  ifstream data {"day04.in"};

  int count_full = 0;
  int count_partial = 0;

  string line, one, two;
  int x1, x2, y1, y2;
  while (data >> line) {
    vector<string> v = split(line, ",");
    one = v[0];
    two = v[1];

    vector<string> v1 = split(one, "-");
    vector<string> v2 = split(two, "-");
    x1 = stoi(v1[0]); x2 = stoi(v1[1]);
    y1 = stoi(v2[0]); y2 = stoi(v2[1]);

    if ((x1 <= y1 && x2 >= y2) || (y1 <= x1 && y2 >= x2)) {
      count_full++;
    }
    if ((x1 <= y1 && y1 <= x2) || (y1 <= x1 && x1 <= y2)) {
      count_partial++;
    }
  }

  return { count_full, count_partial };
}

int main() {
  result res = crunch();
  cout << "part1: " << res.full << '\n';
  cout << "part2: " << res.partial << '\n';
  return 0;
}
