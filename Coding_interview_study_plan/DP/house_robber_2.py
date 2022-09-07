from typing import List


def rob(nums: List[int]) -> int:
	rob_1, rob_2 = 0, 0
	
	for i in range(1, len(nums)):
		temp = max(nums[i] + rob_1, rob_2)
		rob_1 = rob_2
		rob_2 = temp
	a = rob_2
	rob_1, rob_2 = 0, 0
	
	for i in range(len(nums)-1):
		temp = max(nums[i] + rob_1, rob_2)
		rob_1 = rob_2
		rob_2 = temp
	b = rob_2
	return max(a, b)

nums = [2, 7, 9, 3, 1]
print(rob(nums))