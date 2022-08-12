from typing import List

def kthSmallest_noob(matrix: List[List[int]], k:int) -> int:
	matrix = sum(matrix, [])
	matrix.sort()
	return matrix[k-1]

def kthSmallest_quick_select(matrix: List[List[int]], k:int) -> int:
	matrix = sum(matrix, [])
	def quick_select(l, r):
		pivot, p = matrix[r], l
		for i in range(l, r):
			if matrix[i] <= pivot:
				matrix[p], matrix[i] = matrix[i], matrix[p]
				p += 1
		matrix[p], matrix[r] = matrix[r], matrix[p]

		if p > k: return quick_select(l, p-1)
		elif p < k: return quick_select(p+1, r)
		else: return matrix[p]

	return quick_select(0, len(matrix)-2)

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print("from brute force : ", kthSmallest_noob(matrix, k))
print("from quick Select : ", kthSmallest_quick_select(matrix, k))