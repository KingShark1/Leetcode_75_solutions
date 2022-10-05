


def mySqrt(x: int) -> int:
	if x == 1:
		return 1

	result = x

	while(result*result > x):
		result = (result + x // result) >> 1
	
	return result
	
	

n = int(input("Enter Number : "))
print(f"Square root of number : {mySqrt(n)}")