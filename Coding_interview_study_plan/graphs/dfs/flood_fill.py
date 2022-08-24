def floodFill(image, sr, sc, color):
	if not image:
		return [[]]
	source = image[sr][sc]
	visited = set((sr, sc))
	image[sr][sc] = color
	rows, cols = len(image), len(image[0])
	directions = [[1, 0], [-1, 0], [0, 1] ,[0, -1]]
		
	def dfs(r, c):
		for dr, dc in directions:
			row, col = r + dr, c + dc
			if row in range(rows) and col in range(cols): 
				if image[row][col] == source and (row, col) not in visited:
					image[row][col] = color
					visited.add((row, col))
					dfs(row, col)
	dfs(sr, sc)
	return image


image = [[0,0,0],[0,1,0]]
sr = 1
sc = 1
color = 2

print(floodFill(image, sr, sc, color))