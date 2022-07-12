#include <bits/stdc++.h>

using namespace std;

string longestCommonPrefix(vector<string>& strs){
	string ans = "";
	for(int i = 0; i < strs[0].length(); i++){
		for(int j = 1; j < strs.size(); j++){
			if (strs[j][i] != strs[0][i])
				return ans;
		}
		ans.push_back(strs[0][i]);
		
	}
	return ans;
}

int main(){
	vector<string> strs = {"flower","flow","flight"};
	cout<< longestCommonPrefix(strs) << endl;
	return 0;
}