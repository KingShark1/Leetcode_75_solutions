from typing import List

def eraseOverLapIntervals(intervals: List[List[int]]) -> int:
	intervals.sort(key=lambda interval: interval[0])
	count = 0
	j = len(intervals) - 1
	for i in range(len(intervals) - 2, -1, -1):
			print(intervals[j])
			if intervals[i][1] > intervals[j][0]:
					count += 1
			else:
					j = i
	return count

intervals = [[1,2],[1,2],[1,2]]
print(eraseOverLapIntervals(intervals=intervals))