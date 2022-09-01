import heapq
import math

def kClosest(points, k):
  # calculate the distance of each point to origin, save it in hash map.
  # create min heap from the keys of hash map.
  # return top k elements from the values taken from min heap used as index in hashmap.
  if not points:
    return None
  
  def distance(x, y):
    return x**2 + y**2
  
  minHeap = []
  res = []
  for x, y in points:
    dist = distance(x, y)
    minHeap.append([dist, x, y])
  
  heapq.heapify(minHeap)
  
  for i in range(k):
    dist, x, y = heapq.heappop(minHeap)
    res.append([x, y])
  return res

points = [[1,3],[-2,2]]
k = 1
print(kClosest(points, k))
