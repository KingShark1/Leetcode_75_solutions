# Using DP

# Bad Solution!!
# def combinationSum(candidates, target):
# 	length = max(max(candidates)+1, target+1)
# 	dp = [[] for i in range(length)]
# 	for num in candidates:
# 		dp[num].append([num])
# 		for i in range(num, length):
# 			dp[i] = [j+[num] for j in dp[i-num]] + dp[i]
# 	print(dp)
# 	return dp[target]


# Optimized Backtracking
def combinationSum(candidates, target):
	res = []

	def dfs(i, cur, total):
		if total == target:
			res.append(cur.copy())
			return
		if i >= len(candidates) or total > target:
			return
		cur.append(candidates[i])
		dfs(i, cur, total + candidates[i])
		cur.pop()
		dfs(i+1, cur, total)

	dfs(0, [], 0)	
	return res


candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))