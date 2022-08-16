from btree import TreeNode


def lowestCommonAncestor(root, p, q) -> TreeNode:
	# Handle Base case
	if not root or root == p or root == q:
		return root
	
	left = lowestCommonAncestor(root.left, p, q)
	right = lowestCommonAncestor(root.right, p, q)
	if left and right:
		return root
	
	return right if not left else left
	

