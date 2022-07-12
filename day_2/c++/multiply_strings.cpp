#include <bits/stdc++.h>

using namespace std;

string multiply(string num1, string num2){
	if (num1 == "0" or num2 == "0")
		return "0";

	// Reverse num1  and num2
	reverse(num1.begin(), num1.end());
	reverse(num2.begin(), num2.end());

	// Initialize ans as string of zeros with size m + n
	int N = num1.size() + num2.size();
	string ans(N, '0');

	for(int p2 = 0; p2 < num2.size(); p2++){
		int digit2 = num2[p2] - '0';

		for (int p1 = 0; p1 <num1.size(); p1++){
			int digit1 = num1[p1] - '0';
			int numZeros = p1 + p2;
			int carry = ans[numZeros] - '0';
			int multiplication = digit1 * digit2 + carry;

			ans[numZeros] = (multiplication%10) + '0';
			ans[numZeros + 1] += (multiplication / 10);
		}
	}
	if (ans.back() == '0'){
		ans.pop_back();
	}
	reverse(ans.begin(), ans.end());
	return ans;
}

int main(){
	string num1 = "123";
	string num2 = "456";
	cout << multiply(num1, num2)<< endl;
	return 0;
}