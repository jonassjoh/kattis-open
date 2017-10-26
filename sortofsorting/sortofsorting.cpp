#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int custom_cmp(string a, string b) {
	return (a[0] == b[0]) ? a[1] < b[1] : a[0] < b[0];
}

int main() {

	int n;
	while(true) {
		cin >> n;
		if (n == 0) break;

		vector<string> names;

		for (int i=0; i < n; i++) {
			string name;
			cin >> name;
			names.push_back(name);
		}

		stable_sort(names.begin(), names.end(), custom_cmp);

		for (int i=0; i < n; i++) {
			cout << names[i] << endl;
		}
		cout << endl;
	}

	return 0;
}