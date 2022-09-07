from typing import List


def rob(nums: List[int]) -> int:
	rob1, rob2 = 0, 0

	for n in nums:
		temp = max(n+rob1, rob2)
		rob1 = rob2
		rob2 = temp
	
	return rob2
	# # By recursion
	# if len(nums) == 1:
	# 	return nums[0]
	# if not nums:
	# 	return 0
	# if len(nums) == 2:
	# 	return max(nums)

	# max_loot = nums[0] + rob(nums[2:])
	# max_loot = max(max_loot, nums[-1] + rob(nums[:-2]))

	# for i in range(1, len(nums)-1):
	# 	max_loot = max(max_loot, nums[i] + rob(nums[:i-1] + nums[i+2:]))
	# return max_loot

nums = [2, 7, 9, 3, 1]
print(rob(nums))