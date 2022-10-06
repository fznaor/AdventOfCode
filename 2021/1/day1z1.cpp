#include<iostream>
#include<fstream>
using namespace std;

int main11() {
	ifstream in;
	in.open("input.txt");
	int prevDepth, rises = 0;
	in >> prevDepth;
	int depth;
	while (in >> depth) {
		if (depth > prevDepth) rises++;
		prevDepth = depth;
	}
	cout << rises << endl;
	system("pause");
	return 0;
}