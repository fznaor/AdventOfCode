#include<iostream>
#include<string>
#include<fstream>
#include<bitset>
#include<vector>
using namespace std;

int main32()
{
	ifstream in;
	in.open("input3.txt");
	vector<bitset<12>> oxygen, co2;
	bitset<12> b;
	while (in >> b) {
		oxygen.push_back(b);
		co2.push_back(b);
	}
	for (int i = 11; i >= 0; i--) {
		int ones = 0;
		for (int j = 0; j < oxygen.size(); j++) {
			if (oxygen[j][i])ones++;
		}
		bool toDelete;
		if (ones >= oxygen.size() / 2.0)toDelete = false;
		else toDelete = true;
		for (int j = oxygen.size() - 1; j>=0; j--) {
			if (oxygen[j][i] == toDelete)oxygen.erase(oxygen.begin() + j);
		}
		if (oxygen.size() == 1)break;
	}
	for (int i = 11; i >= 0; i--) {
		int ones = 0;
		for (int j = 0; j < co2.size(); j++) {
			if (co2[j][i])ones++;
		}
		bool toDelete;
		if (ones < co2.size() / 2.0)toDelete = false;
		else toDelete = true;
		for (int j = co2.size() - 1; j >= 0; j--) {
			if (co2[j][i] == toDelete)co2.erase(co2.begin() + j);
		}
		if (co2.size() == 1)break;
	}
	cout << co2[0].to_ulong() * oxygen[0].to_ulong() << endl;
	system("pause");
	return 0;
}