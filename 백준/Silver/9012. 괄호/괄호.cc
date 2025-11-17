#include <iostream>
#include <stack>
using namespace std;

int main() {
	string bracket;
	int T;
	int bracket_size = 0;
	string result;

	cin >> T;
	for (int i = 0; i < T; i++) {
		stack<char> s;
		result = "YES";

		cin >> bracket;
		bracket_size = bracket.size();

		for (int j = 0; j < bracket_size; j++) {
			if (bracket[j] == '(') {
				s.push('(');
			}
			else if (bracket[j] == ')') {
				if (!s.empty()) {
					s.pop();
				}
				else result = "NO";
			}
		}
		if (!s.empty()) {
			result = "NO";
		}
		cout << result << endl;
	}
}