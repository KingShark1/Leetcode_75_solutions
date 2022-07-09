#include <bits/stdc++.h>

using namespace std;

bool isHappy(int n){
	int sum = 0;
	int rem;
	while(n > 0){
		rem = n % 10;
		sum += rem * rem;
		n /= 10;
	}
	if (sum == 1)
		return true;
	else if (sum == 4 or sum == 9)
		return false;
	else
		return isHappy(sum);
}

int main(){
	int input;
	cout << "Enter n\n";
	cin >> input;

	cout << isHappy(input) << '\n';
	return 0;
}