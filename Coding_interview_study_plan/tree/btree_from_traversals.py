from btree import TreeNode

def checkTree(a, b) -> bool:
	if not a and not b:
		return True
	if not a or not b:
		return False
	if a.val == b.val:
		return checkTree(a.left, b.left) and checkTree(a.right, b.right)

def buildTree(preorder, inorder):
	if not preorder or not inorder:
		return None
	root = TreeNode(preorder[0])
	mid = inorder.index(preorder[0])
	root.left = buildTree(preorder[1:mid+1], inorder[:mid])
	root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
	return root
	
preorder, inorder = [3,9,20,15,7], [9,3,15,20,7]
newroot = buildTree(preorder, inorder)
d = TreeNode(7)
c = TreeNode(15)
b = TreeNode(20, c, d)
a = TreeNode(9)
root = TreeNode(3, a, b)

print(checkTree(newroot, root))