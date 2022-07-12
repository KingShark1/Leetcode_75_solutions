## [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
Logic : Brute Force O(n*m) where n = size of input array, m = length of first string

- Loop over first string for all its characters
- Loop over the entire array.
- whenever the characters dont match, return ans (ans is initialized to be an empty string)
- finally return ans

#### Runtime : 3ms
#### Memory Usage : 9.1MB

## [Multiply Strings](https://leetcode.com/problems/multiply-strings/)
Logic : Critical Thinking | Time : O(n*m) n = digits in num1 m = digits in num 2

- Reverse both numbers
- Initialize answer with n + m zeros
- for each digit at position i in num 2 :
	- for each digit at position j in num 1:
		- multiply the digit from num 2 by the digit from num 1 and add previously carried balue to the multiplication result.
		- Take the remainder of multiplication with 10 to get the ones place digit of the multiplication result.
		- Put the last digit at the current position (i+j) in the answer.
		-	Divide the multiplication by 10 to get the new value for carry and add it to answer at the next position. 
		- if the last digit in answer is zero, before reversing answer, we must pop the zero from answer. Otherwise there'd be a leading zero in the final answer.
		- Reverse answer and return it
