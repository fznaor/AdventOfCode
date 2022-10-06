#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string>
#include<stack>
using namespace std;

int main101() {
	ifstream in;
	in.open("v21.txt");
	string line;
	unsigned long long res = 0;
	while (getline(in, line)) {
		stack<char> s;
		for (char c : line) {
			if (c == '(' || c == '[' || c == '{' || c == '<') {
				s.push(c);
			}
			else {
				bool error = false;
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
					if (c == ')')res += 3;
					else if (c == ']')res += 57;
					else if (c == '}')res += 1197;
					else if (c == '>')res += 25137;
				}
			}
		}
	}
	cout << res << endl;
	system("pause");
	return 0;
}