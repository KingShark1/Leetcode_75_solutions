import heapq


class MedianFinder:
	def __init__(self) -> None:
		"""
		Initialize your data structure here
		two heaps, Large, small, min heap, max heap
		Heaps should be equal size
		"""
		self.small, self.large = [], []

	def addNum(self, num) -> None:
		heapq.heappush(self.small, -1*num)

		# Pop from small heap and add to large heap
		if self.small and self.large and -1*self.small[0] > self.large[0]:
			val = -1*heapq.heappop(self.small)
			heapq.heappush(self.large, val)

		if len(self.small) > len(self.large) + 1:
			val = -1*heapq.heappop(self.small)
			heapq.heappush(self.large, val)
		
		if len(self.large) > len(self.small) + 1:
			val = heapq.heappop(self.large)
			heapq.heappush(self.small, -1*val)

	def findMedian(self) -> float:
		if len(self.small) > len(self.large):
			return -1*self.small[0]
		if len(self.large) > len(self.small):
			return self.large[0]
		return (-1*self.small[0] + self.large[0]) / 2

def main():
	medianFinder = MedianFinder()
	medianFinder.addNum(1)    
	medianFinder.addNum(2)
	print(medianFinder.findMedian())
	medianFinder.addNum(3)
	print(medianFinder.findMedian())

if __name__ == "__main__":
	main()