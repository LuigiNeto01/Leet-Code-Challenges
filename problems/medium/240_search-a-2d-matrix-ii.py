from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        # Start from top-right corner (or bottom-left would work too)
        # Top-right gives us two clear directions:
        # - If current > target, move left (smaller values)
        # - If current < target, move down (larger values)
        row, col = 0, n - 1
        
        while row < m and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True
            elif current > target:
                # Target must be to the left (smaller values in row)
                col -= 1
            else:
                # Target must be below (larger values in column)
                row += 1
        
        # Target not found after exhausting search space
        return False