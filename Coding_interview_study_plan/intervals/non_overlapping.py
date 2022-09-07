from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
	# Sort the array,
	# return the difference between size of original array and new array
	intervals = sorted(intervals) # O(nlogn)
	

intervals = [[1,2],[2,3]]
print(eraseOverlapIntervals(intervals=intervals))