from btree import TreeNode

def maxPathSum(root) -> int:
	res = [root.val]

	def dfs(root):
		if not root:
			return 0
		
		left = max(0, dfs(root.left))
		right = max(0, dfs(root.right))

		# Compute sum with splis
		res[0] = max(res[0], root.val + left + right)
		return root.val + max(left, right)
	dfs(root)
	return res[0]


d = TreeNode(7)
c = TreeNode(15)
b = TreeNode(20, c, d)
a = TreeNode(9)
root = TreeNode(-10, a, b)
print(maxPathSum(root))