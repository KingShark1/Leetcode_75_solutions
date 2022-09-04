from typing import List
from merge_intervals import merge
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
	res = []
	for i in range(len(intervals)):
		if newInterval[1] < intervals[i][0]:
			res.append(newInterval)
			return res + intervals[i:]
		elif newInterval[0] > intervals[i][1]:
			res.append(intervals[i])
		else:
			newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
	res.append(newInterval)
	return res

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
output = [[1,2],[3,10],[12,16]]
print(insert(intervals=intervals, newInterval=newInterval))