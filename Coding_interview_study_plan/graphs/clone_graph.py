# Definition for a Node.
from collections import deque


class Node:
	def __init__(self, val = 0, neighbors = None):
		self.val = val
		self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
	if not node:
		return node

	q, clones = deque([node]), {node.val: Node(node.val, [])}
	while q:
		cur = q.popleft()
		cur_clone = clones[cur.val]
		
		for ngbr in cur.neighbors:
			if ngbr.val not in clones:
				clones[ngbr.val] = Node(ngbr.val, [])
				q.append(ngbr)
			cur_clone.neighbors.append(clones[ngbr.val])
	return clones[node.val]

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.neighbors = [b, d]
b.neighbors = [a, c]
c.neighbors = [b, d]
d.neighbors = [a, c]  