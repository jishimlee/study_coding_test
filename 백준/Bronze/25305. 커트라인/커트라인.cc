#include <iostream>
using namespace std;

void swap(int& a, int& b) {
	int temp = a;
	a = b;
	b = temp;
}

void selectionSort(int list[], int n) {
	int least;
	for (int i = 0; i < n - 1; i++) {
		least = i;
		for (int j = i + 1; j < n; j++) {
			if (list[least] < list[j]) {
				least = j;
			}
		}
		swap(list[i], list[least]);
	}
}

int main() {
	int n;
	int data[1000];
	int k;
	cin >> n >> k;

	for (int i = 0; i < n; i++) {
		cin >> data[i];
	}

	selectionSort(data, n);

	cout << data[k - 1] << endl;

	return 0;
}