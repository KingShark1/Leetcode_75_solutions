from typing import List

def sortColors(nums: List[int]) -> None:
	l, r = 0, len(nums)-1
	i = 0

	def swap(i, j):
		# input : index for swap
		# function : swaps element of the array in place, given index
		# returns : nothing
		nums[i], nums[j] = nums[j], nums[i]
		
	while i <= r:
		if nums[i] == 0:
			swap(l, i)
			l += 1

		elif nums[i] == 2:
			swap(i, r)
			r -= 1
			i -= 1
		
		i += 1
	
	return nums
	
nums = [2,0,2,1,1,0]
print(sortColors(nums))