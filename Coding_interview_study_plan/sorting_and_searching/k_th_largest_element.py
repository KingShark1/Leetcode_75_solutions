from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
	k = len(nums) - k
	def quick_select(l, r) -> int:
		pivot, p = nums[r], l
		for i in range(l, r):
			if nums[i] <= pivot:
				nums[i], nums[p] = nums[p], nums[i]
				p+=1
		nums[p], nums[i] = nums[i], nums[p]
		if p > k: return quick_select(l, p-1)
		elif p < k: return quick_select(p+1, r)
		else: return nums[p]
	
	return quick_select(0, len(nums)-1)

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))
