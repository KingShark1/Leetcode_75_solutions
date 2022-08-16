from lib2to3.pgen2.token import OP
from typing import Optional
from btree import TreeNode

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
	# Recursion

	# Checking for base case : Empty root
	if not root:
		return None
	
	# Recurse
	root.left, root.right = invertTree(root.right), invertTree(root.left)
	return root

