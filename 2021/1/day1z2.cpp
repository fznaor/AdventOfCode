#include<iostream>
#include<fstream>
using namespace std;

int main12() {
	ifstream in;
	in.open("input.txt");
	int depthA, depthB, depthC, rises = 0, newDepth;
	in >> depthA;
	in >> depthB;
	in >> depthC;
	while (in >> newDepth) {
		if (newDepth > depthC) rises++;
		depthC = depthB;
		depthB = depthA;
		depthA = newDepth;
	}
	cout << rises << endl;
	system("pause");
	return 0;
}