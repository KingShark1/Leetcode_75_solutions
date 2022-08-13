from typing import List

def setZeros(matrix: List[List[int]]):
	m, n, row, col = len(matrix), len(matrix[0]), [], []
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				row.append(i)
				col.append(j)
	for i in range(m):
		for j in range(n):
			if i in row or j in col:
				matrix[i][j] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeros(matrix)
print(matrix)