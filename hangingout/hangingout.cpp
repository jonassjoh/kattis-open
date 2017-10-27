#include <iostream>
using namespace std;

int main() {

	int L, x;
	cin >> L >> x;

	int res = 0;
	int party = 0;
	string type;
	int amount;
	for (int i=0; i < x; i++) {
		cin >> type >> amount;
		if (type[0] != 'e')
			amount *= -1;

		party += amount;
		if (party > L) {
			party -= amount;
			res++;
		}
	}

	cout << res << endl;

	return 0;
}