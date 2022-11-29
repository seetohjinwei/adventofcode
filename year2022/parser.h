#include <string>
#include <vector>
#pragma once

using namespace std;

const string SPACE = " ";

vector<string> readFile(const string&);
vector<string> split(const string&, const string& = SPACE);
