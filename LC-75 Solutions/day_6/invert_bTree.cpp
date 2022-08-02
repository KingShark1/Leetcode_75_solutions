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
	if(root->left != NULL)
		cout << root->left->val << ' ';
	if(root->right != NULL)
		cout << root->right->val << ' ';
}

TreeNode* invertTree(TreeNode* root){
	TreeNode* tmp;
	// Base Case
	if(!root or(!root->left and !root->right)) return root;
	TreeNode* left = invertTree(root->left);
	TreeNode* right = invertTree(root->right);
	root->left = right;
	root->right = left;
	return root;
}

int main(){
	TreeNode c(3);
	TreeNode a(1);
	TreeNode g(9);
	TreeNode f(6);
	TreeNode b(2, &a, &c);
	TreeNode e(7, &f, &g);
	TreeNode d(4, &b, &e);

	printTree(invertTree(&d));
	return 0;
}
