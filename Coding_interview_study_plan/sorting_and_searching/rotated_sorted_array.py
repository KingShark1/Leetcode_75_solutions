from selectors import EpollSelector
from typing import List

def search(nums:List[int], target) -> int:
	start = 0
	end = len(nums)-1
	
	while start <= end:
		mid = (start+end)//2

		if target == nums[mid]:
			return mid
			
		elif nums[start] <= nums[mid]:
					
			if target < nums[start] or target > nums[mid]:
				start = mid+1
			else:
				end = mid-1
		else:
			if target > nums[end] or target < nums[mid]:
				end = mid-1
			else:
				start = mid+1
							
	return -1
nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))