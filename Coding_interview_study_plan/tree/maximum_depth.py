from btree import TreeNode
from typing import Optional

def maxDepth(root: Optional[TreeNode]) -> int:
	if not root:
		return 0
	def getDepth(node: Optional[TreeNode]) -> int:
		# returns depth starting from the given node
		if not node.left or not node.right:
			if not node.left and node.right:
				return 1 + getDepth(node.right)
			elif not node.right and node.left:
				return 1 + getDepth(node.left)
			if not node.left and not node.right:
				return 1
		else:
			return 1 + max(getDepth(node.left), getDepth(node.right))
	return getDepth(root)

d = TreeNode(7)
c = TreeNode(15)
b = TreeNode(20, c, d)
a = TreeNode(9)
root = TreeNode(3, a, b)
print(maxDepth(root))