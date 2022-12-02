#include "definitions.h"
#include "parser.h"
#include <fstream>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

unordered_map<char, int> scoring = {
  {'A', 1},
  {'B', 2},
  {'C', 3},
  {'X', 1},
  {'Y', 2},
  {'Z', 3}
};

const ll lose = 0L;
const ll draw = 3L;
const ll win = 6L;

ll part1() {
  ifstream data {"day02.in"};

  ll score = 0L;

  char c, d;
  int x, y;
  while (data >> c >> d) {
    x = scoring[c], y = scoring[d];

    if (x == y)
      score += y + draw;
    else if ((y - x + 3) % 3 == 1)
      score += y + win;
    else
      score += y + lose;
  }

  return score;
}

ll part2() {
  ifstream data {"day02.in"};

  ll score = 0L;

  char c, d;
  int x, y, z;
  while (data >> c >> d) {
    x = scoring[c], y = scoring[d];

    switch (y) {
      case 1:
        z = (x - 2 + 3) % 3 + 1;
        score += z + lose;
        break;
      case 2:
        z = x;
        score += z + draw;
        break;
      case 3:
        z = x % 3 + 1;
        score += z + win;
        break;
    }
  }

  return score;
}

int main() {
  cout << "part 1: " << part1() << endl;
  cout << "part 2: " << part2() << endl;

  return 0;
}
