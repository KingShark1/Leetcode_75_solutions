from typing import Optional, List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, row in enumerate(matrix):
            if target in row:
                return True
                break
            
