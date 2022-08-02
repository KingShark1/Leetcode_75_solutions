## [Happy Number](https://leetcode.com/problems/happy-number/)
Logic : Recursion
- Run loop to find all the digits in the given number, square them and add them up
- BASE CASE : if sum equals 1, return True, else if sum equals 4 or 9 return False (as any other integer would have it's square greater than 9 and thus the recursion would go further)
- RECURSION CASE : if sum equals any other integer than 1, recurse.

#### Runtime : 0ms
#### Memory Usage : 6MB

## [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
Logic : Looping (Brute Force)
- Create 4 pointers pointing to current start and end row, along with current start and end columns.
- Create 4 loops, for going right, then down ,then left, then up.
- return the answer when total number of elements observed equals total elements given in the spiral matrix

#### Runtime : 0 ms
#### Memory Usage : 7MB

## [Where will the ball fall?](https://leetcode.com/problems/where-will-the-ball-fall/)
Logic : DFS + Recursion
- if top = 1, this means we are in upper part of grid in ith row and jth column.
	- if grid(i)(j) = 1
		- We have to go to the bootom part of right cell, if that is out of bounds return -1.
		- if grid(i)(j+1) is not 1 then we cannot go further and are blocked, return -1.
	- if grid(i)(j) = -1
		- We have to go to the bootom part of left cell, if that is out of bounds return -1.
		- if grid(i)(j-1) is not 1 then we cannot go further and are blocked, return -1.
- if top = 0 this means we are in the lower part of grid(i)(j). In such case no matter the value of current  cell, we need to go down.
- If we reach the bootom part of last row, then return column number.
- !top means in next function call state will change from top to bottom and vice versa.

#### Runtime : 48 ms
#### Memory Usage : 13.3MB