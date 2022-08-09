from typing import List

def trap_water(arr: List[int])->int:
	if not arr: return 0
	
	res = 0
	left, right = 0, len(arr)-1
	maxL, maxR = arr[left], arr[right]
	
	while left<right:
		if maxL < maxR:
			left += 1
			maxL = max(maxL, arr[left])
			res += maxL - arr[left]
		else:
			right -= 1
			maxR = max(maxR, arr[right])
			res += maxR - arr[right]
	return res

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap_water(arr))