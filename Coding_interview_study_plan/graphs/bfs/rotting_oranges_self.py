from collections import deque


def orangesRotting(grid) -> int:
  rows, cols = len(grid), len(grid[0])
  directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
  visited = set()
  q = deque()
  fresh = 0
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 2:
        q.append((i, j))
        visited.add((i, j))
      elif grid[i][j] == 1:
        fresh += 1
  
  def check_adjacent(r, c):
    for dr, dc in directions:
      row, col = r + dr, c + dc
      if row in range(rows) and col in range(cols) and (row, col) not in visited and grid[row][col] == 1:
        visited.add((row, col))
        q.append((row, col))  
        fresh -= 1  
    
  time = 0
  while q and fresh > 0:
    breadth = len(q)
    for i in range(breadth):
      r, c = q.pop()
      check_adjacent(r, c)
    time += 1
  
  
  
  return time if fresh == 0 else -1
 
grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))