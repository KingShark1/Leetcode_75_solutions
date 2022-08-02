def lengthOfLongestSubstring(s: str) -> int:
	l, r = 0, 0
	curSet = set()  # a set to store strings with no duplicates
	ans = 0  # the maximum length
	while r < len(s):
	# keep shrinking the window until s[r] has no duplicates in the current set
			while s[r] in curSet:
					curSet.remove(s[l])  # update the set
					l += 1  # shrink the window
			# then s[r] can be added in to the current set
			curSet.add(s[r])
			ans = max(ans, len(curSet))  # update max length
			r += 1
	return ans

s = input("Enter string\n")
print(f"longest substring is of length {lengthOfLongestSubstring(s)}")