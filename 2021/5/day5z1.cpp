#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string>
#include<map>
using namespace std;

int main51() {
	ifstream in;
	in.open("v21.txt");
	string line;
	map<pair<int, int>, int> points;
	int res = 0;
	while (getline(in, line)) {
		int x1, y1, x2, y2;
		sscanf(line.c_str(), "%d,%d -> %d,%d", &x1, &y1, &x2, &y2);
		if (x1 == x2) {
			int lower, upper;
			if (y1 < y2) {
				lower = y1;
				upper = y2;
			}
			else {
				lower = y2;
				upper = y1;
			}
			for (int i = lower; i <= upper; i++) {
				if (points.count(make_pair(x1, i)) == 0) {
					points.insert(make_pair(make_pair(x1, i), 1));
				}
				else {
					points[make_pair(x1, i)]++;
					if (points[make_pair(x1, i)] == 2)
						res++;
				}
			}
		}
		else if (y1 == y2) {
			int lower, upper;
			if (x1 < x2) {
				lower = x1;
				upper = x2;
			}
			else {
				lower = x2;
				upper = x1;
			}
			for (int i = lower; i <= upper; i++) {
				if (points.count(make_pair(i, y1)) == 0) {
					points.insert(make_pair(make_pair(i, y1), 1));
				}
				else {
					points[make_pair(i, y1)]++;
					if (points[make_pair(i, y1)] == 2)
						res++;
				}
			}
		}
		else {
			int lowerx, upperx, y;
			bool yGrowing;
			if (x1 < x2) {
				lowerx = x1;
				upperx = x2;
				y = y1;
				if (y1 < y2)yGrowing = true;
				else yGrowing = false;
			}
			else {
				lowerx = x2;
				upperx = x1;
				y = y2;
				if (y1 < y2)yGrowing = false;
				else yGrowing = true;
			}
			for (int i = lowerx; i <= upperx; i++) {
				if (points.count(make_pair(i, y)) == 0) {
					points.insert(make_pair(make_pair(i, y), 1));
				}
				else {
					points[make_pair(i, y)]++;
					if (points[make_pair(i, y)] == 2)
						res++;
				}
				if (yGrowing)y++;
				else y--;
			}
		}
	}
	cout << res << endl;
	system("pause");
	return 0;
}