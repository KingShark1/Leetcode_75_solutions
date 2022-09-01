import heapq
from typing import List
"""
  Using Heaps to return top k frequent
"""
def topKFrequent(nums: List[int], k: int):
  if not nums:
    return []
  
  count = {}
  for i in range(len(nums)):
    if nums[i] not in count:
      count[nums[i]] = 1
    else:
      count[nums[i]] += 1

  invcount = {}
  for num in count:
    invcount.setdefault(-1 * count[num], []).append(num)
  
  heap = list(invcount.keys())
  heapq.heapify(heap)
  res = []
  
  while k:
    elem = heapq.heappop(heap)
    for num in invcount[elem]:
      res.append(num)
      k -= 1
  return res

nums = [1,1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))