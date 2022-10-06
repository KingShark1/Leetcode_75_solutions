def maxArea(height) -> int:
	low, high = 0, len(height) -1
	m = 0
	dist = high - low
	while(low < high):
		if height[low] < height[high]:
			m = max(m, dist*height[low])
			low += 1
		else:
			m = max(m, dist*height[high])
			high -= 1
		
		dist -= 1
	
	return m

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

