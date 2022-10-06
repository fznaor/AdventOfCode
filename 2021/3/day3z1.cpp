#include<iostream>
#include<string>
#include<fstream>
#include<bitset>
using namespace std;

int main31()
{
	ifstream in;
	in.open("input3.txt");
	bitset<12> b, gamma, epsilon;
	int ones[12]{}, lines = 0;
	while (in >> b) {
		for (int i = 0; i < 12; i++) {
			if (b[i])ones[i]++;
		}
		lines++;
	}
	for (int i = 0; i < 12; i++) {
		if (ones[i] > lines / 2)gamma[i] = true;
		else gamma[i] = false;
		epsilon[i] = !gamma[i];
	}
	cout << gamma.to_ulong() * epsilon.to_ulong() << endl;
	system("pause");
	return 0;
}