import time

def climbStairs(n: int) -> int:
	start = time.time()
	one, two = 1, 1

	for i in range(n-1):
		temp = one
		one = one + two
		two = temp
	finish = time.time()
	print(finish - start)
	return one

n = 10
climbStairs(n)