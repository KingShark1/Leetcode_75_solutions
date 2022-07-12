## [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
Logic : Brute Force O(n*m) where n = size of input array, m = length of first string

- Loop over first string for all its characters
- Loop over the entire array.
- whenever the characters dont match, return ans (ans is initialized to be an empty string)
- finally return ans

#### Runtime : 3ms
#### Memory Usage : 9.1MB