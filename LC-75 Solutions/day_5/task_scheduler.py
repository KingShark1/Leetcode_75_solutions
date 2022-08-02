import heapq
from collections import Counter, deque

def leastInterval(tasks, n: int) -> int:
	# Each task takes 1 unit of time
	# minimize idle time
	count = Counter(tasks)
	maxHeap = [-cnt for cnt in count.values()]
	heapq.heapify(maxHeap)

	time = 0
	q = deque() # pairs of [-cnt, idleTime]
	
	while maxHeap or q:
		time += 1

		if maxHeap:
			cnt = 1 + heapq.heappop(maxHeap)
			if cnt:
				q.append([cnt, time + n])
		
		if q and q[0][1] == time:
			heapq.heappush(maxHeap, q.popleft()[0])
		
	return time
	
def main():
	tasks = ["A","A","A","B","B","B"],
	n = 2
	print(leastInterval(tasks, n))

if __name__=="__main__":
	main()