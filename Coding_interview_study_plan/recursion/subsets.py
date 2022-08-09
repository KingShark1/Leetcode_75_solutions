from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
	res = [[]]
	
	def combine(arr, res):
		if not arr: return
		res.append(arr)
		for i in range(len(arr)):
			if arr[:i] + arr[i+1:] not in res:
				combine(arr[:i] + arr[i+1:], res)
		return 
		
	combine(nums, res)
	return res

nums = [1, 2, 3]
print(subsets(nums))