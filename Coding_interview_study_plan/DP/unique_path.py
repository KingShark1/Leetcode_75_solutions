def uniquePaths(m, n):
	dp = [[0]*n]*m
	dp[0][-1] = 1
	dp[-1] = [1 for j in range(n)]
	
	for i in range(m-2, -1, -1):
		for j in range(n-2, -1, -1):
			dp[i][j] = dp[i+1][j] + dp[i][j+1]
	
	return dp[0][0]

m, n = 3, 7
print(uniquePaths(m, n))
