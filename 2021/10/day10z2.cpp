#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<stack>
#include<algorithm>
using namespace std;

int main() {
	ifstream in;
	in.open("v21.txt");
	string line;
	unsigned long long res = 0;
	vector<long long>scores;
	while (getline(in, line)) {
		stack<char> s;
		bool error = false;
		for (char c : line) {
			if (c == '(' || c == '[' || c == '{' || c == '<') {
				s.push(c);
			}
			else {
				char open = s.top();
				s.pop();
				if (open == '(' && c != ')') {
					error = true;
				}
				else if (open == '[' && c != ']') {
					error = true;
				}
				else if (open == '{' && c != '}') {
					error = true;
				}
				else if (open == '<' && c != '>') {
					error = true;
				}
				if (error) {
					break;
				}
			}
		}
		long long score = 0;
		if (!error) {
			while (!s.empty()) {
				score *= 5;
				if (s.top() == '(')
					score += 1;
				else if (s.top() == '[')
					score += 2;
				else if (s.top() == '{')
					score += 3;
				else score += 4;
				s.pop();
			}
			scores.emplace_back(score);
		}
	}
	sort(scores.begin(), scores.end());
	cout << scores[scores.size()/2] << endl;
	system("pause");
	return 0;
}