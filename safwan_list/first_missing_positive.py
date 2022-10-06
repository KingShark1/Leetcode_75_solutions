import sys

def firstMissingPostive(nums) -> int:
	for i in range(len(nums)):
		if nums[i] <= 0: nums[i] = sys.maxsize
	
	for i in nums:
		if i < 0: i *= -1
		if (i - 1 < len(nums) and nums[i-1] > 0):
			nums[i-1] *= -1
	
	for i in range(len(nums)):
		if nums[i] >= 0: return i+1

	return len(nums) + 1
		
nums = [3,4,-1,1]
print(firstMissingPostive(nums))