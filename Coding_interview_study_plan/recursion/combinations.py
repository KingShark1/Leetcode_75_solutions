from typing import List
from unittest import result


def combine(n: int, k:int)-> List[List[int]]:
	if (n,k) == (1, 1): return [[1]]
	res = [[]]
	sub = []

	def backtrack(start, n, k, sub, res):
		if(len(sub) == k):
			res.append(sub)
			return
		
		for i in range(start, n - k + len(sub) + 1):
			sub.append(i)
			backtrack(i+1, n, k, sub, res)
			sub.pop()

	backtrack(1, n, k, sub, res)
	return res

n, k = 4, 2
print(combine(n, k))