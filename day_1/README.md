## [Happy Number](https://leetcode.com/problems/happy-number/)
Logic : Recursion
- Run loop to find all the digits in the given number, square them and add them up
- BASE CASE : if sum equals 1, return True, else if sum equals 4 or 9 return False (as any other integer would have it's square greater than 9 and thus the recursion would go further)
- RECURSION CASE : if sum equals any other integer than 1, recurse.

#### Runtime : 0ms
#### Memory Usage : 6MB