#include <bits/stdc++.h>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int ans = 0;

int dfs(TreeNode* root){
	if(!root) return -1;

	int left = dfs(root->left);
	int right = dfs(root->right);
	ans = max(ans, 2+left+right);
	return 1 + max(left, right);
}

int diameterOfBinaryTree(TreeNode* root) {
	dfs(root);
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

	cout << diameterOfBinaryTree(&d) << '\n';
	return 0;
}