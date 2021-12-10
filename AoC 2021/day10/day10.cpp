#include <iostream>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

#define ll long long
#define ld long double

int main(int argc, char const *argv[])
{
    freopen("a.in", "r", stdin);
    unordered_map<char, ll> table1 =
        {
            {')', 3},
            {']', 57},
            {'}', 1197},
            {'>', 25137},
        };
    unordered_map<char, char> chunk =
        {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'},
            {'<', '>'},
        };
    unordered_map<char, ll> table2 =
        {
            {'(', 1},
            {'[', 2},
            {'{', 3},
            {'<', 4},
        };
    ll part1 = 0;
    vector<ll> part2;
    string line;
    while (getline(cin, line))
    {
        bool corrupt = false;
        stack<char> s;
        for (char c : line)
        {
            if (chunk.find(c) != chunk.end())
            {
                s.push(c);
            }
            else
            {
                if (chunk[s.top()] != c)
                {
                    part1 += table1[c];
                    corrupt = true;
                    break;
                }
                s.pop();
            }
        }
        if (!corrupt)
        {
            ll stringScore = 0;
            while (!s.empty())
            {
                stringScore = stringScore * 5 + table2[s.top()];
                s.pop();
            }
            part2.push_back(stringScore);
        }
    }
    sort(part2.begin(), part2.end());
    cout << part1 << '\n';
    cout << part2[part2.size() / 2] << '\n';
    return 0;
}
