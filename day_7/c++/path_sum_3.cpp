#include <bits/stdc++.h>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

unordered_map<long long, long long> mp;
long long ans = 0;

void count(TreeNode* root, long long csum, long long tar){
	if(root == NULL) return;

	csum += root->val;

	if(csum == tar) ans++;
	if(mp.find(csum-tar)!=mp.end()) ans+=mp[csum-tar];
        
	mp[csum]++;
	count(root->left, csum, tar);
	count(root->right, csum, tar);

	mp[csum]--;
	return;
}

int pathSum(TreeNode* root, int targetSum){
	count(root, 0, targetSum);
	return ans;
}

int main(){
	TreeNode c(3);
	TreeNode a(1);
	TreeNode g(9);
	TreeNode f(6);
	TreeNode b(2, &a, &c);
	TreeNode e(7, &f, &g);
	TreeNode d(4, &b, &e);

	cout << pathSum(&d, 7) << '\n';
	return 6;
}


