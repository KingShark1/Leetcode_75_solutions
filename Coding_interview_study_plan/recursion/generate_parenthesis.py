from typing import List

def generate(ans, s, open, close):
	if open == 0 and close == 0:
		ans.append(s)
	
	if open > 0:
		generate(ans, s+'(', open-1, close)
	
	if(open < close):
		generate(ans, s+')', open, close-1)

def generate_parenthesis(n: int) -> List[str]:
	ans = []
	generate(ans, '', n, n)
	return ans

n = int(input())
print(generate_parenthesis(n))