from typing import List


def coinChange(coins: List[int], amount: int) -> int:
	dp = [amount + 1] * (amount + 1)
	# Base case
	dp[0] = 0

	for a in range(1, amount+1):
		for c in coins:
			if a - c >= 0:
				dp[a] = min(dp[a], 1 + dp[a-c])
	
	return dp[amount] if dp[amount] != amount + 1 else -1



coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 10000]
amount = 999999
print(coinChange(coins, amount))