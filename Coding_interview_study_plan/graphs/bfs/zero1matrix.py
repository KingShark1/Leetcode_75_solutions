import sys
import collections

def updateMatrix(mat):
	"""
	Given m*n binary matrix "mat".
	Returns the distance of the nearest 0 for each cell
	"""
	# Handling empty matrix
	if not mat:
		return [[]]
	rows, cols = len(mat), len(mat[0])
	directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
	q = collections.deque()

	for r in range(rows):
		for c in range(cols):
			if mat[r][c] == 0:
				q.append((r, c))
				continue
			mat[r][c] = float('inf')
	
	while q:
		k = len(q)
		for i in range(k):
			r, c = q.popleft()
			dist = mat[r][c]
			for dr, dc in directions:
				row, col = r + dr, c + dc
				if row not in range(rows) or col not in range(cols) or mat[row][col] == 0:
					continue
				if dist + 1 < mat[row][col]:
					mat[row][col] = dist + 1
					q.append((row, col))

	return mat

mat = [[0,0,0],[0,1,0],[1, 1, 1]]
print(updateMatrix(mat))