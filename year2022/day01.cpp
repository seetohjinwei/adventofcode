#include "definitions.h"
#include "parser.h"
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

ll solve(int count) {
  vector<string> lines = readFile("day01.in");

  priority_queue<ll> pq;
  ll current = 0;

  for (auto s : lines) {
    if (s == "") {
      pq.push(current);
      current = 0;
      continue;
    }
    ll calories = stoll(s);
    current += calories;
  }
  pq.push(current);

  ll total = 0;
  while (count--) {
    total += pq.top();
    pq.pop();
  }

  return total;
}

int main() {
  cout << "part 1: " << solve(1) << endl;
  cout << "part 2: " << solve(3) << endl;

  return 0;
}
