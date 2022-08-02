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

void printTree(TreeNode* root){
	cout << root->val << '\n';		
	cout << root->left->val << ' ';
	if(root->right != NULL)
		cout << root->right->val << ' ';
}

int dfs(TreeNode* root){
	if(!root) return 0;

	int l = dfs(root->left);
	if(l == -1) return -1;

	int r = dfs(root->right);
	if(r == -1) return -1;

	if(abs(l-r) > 1) return -1;
	return 1+max(l, r);
}

bool isBalanced(TreeNode* root){
	if(dfs(root) == -1) return false;
	else return true;
}

int main(){
	TreeNode c(3);
	TreeNode a(1);
	TreeNode g(9);
	TreeNode f(6);
	TreeNode b(2, &a, &c);
	TreeNode e(7, &f, &g);
	TreeNode d(4, &b, &e);

	cout << isBalanced(&d) << '\n';
	return 0;
}