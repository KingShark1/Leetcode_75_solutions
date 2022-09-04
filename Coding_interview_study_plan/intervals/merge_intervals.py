from collections import deque
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
	intervals = sorted(intervals)
	def is_overlap(a, b):
		return a[0] <= b[1] and b[0] <= a[1]
	
	def merge_overlapping(a, b):
		return [min(a[0], b[0]), max(a[1], b[1])]
	
	res = []
	res.append(intervals[0])
	for i in range(1, len(intervals)):
		if is_overlap(res[-1], intervals[i]):
			res[-1] = merge_overlapping(res[-1], intervals[i])
		else:
			res.append(intervals[i])
	return res





# intervals1 = [[2,6], [1,3],[8,10],[15,18]]
# intervals2 = [[5,5],[1,2],[2,4],[2,3],[4,4],[5,5],[2,3],[5,6],[0,0],[5,6]]

# # print(merge(intervals=intervals1))
# print(merge(intervals=intervals2))