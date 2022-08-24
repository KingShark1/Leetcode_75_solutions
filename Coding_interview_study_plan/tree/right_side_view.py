import collections
from btree import TreeNode


def rightSideView(root):
	res = []
	q = collections.deque([root])
	while q:
		rightSide = q.popleft()
		level = len(q)
		for i in range(level):
			node = q.popleft()
			if node:
				rightSide = node
				q.append(node.left)
				q.append(node.right)
		if rightSide:
			res.append(rightSide.val)
	return res

e = TreeNode(4)
d = TreeNode(5)
c = TreeNode(3, right=e)
b = TreeNode(2, right=d)
root = TreeNode(1, b, c)

"""
		1	<-
	2		3 <-
		5		4	<-
"""
print(rightSideView(root))