from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)  # number of rows
        n = len(matrix[0])  # number of columns
        
        # Treat the 2D matrix as a 1D sorted array
        # Total elements = m * n
        # For index i in 1D array: row = i // n, col = i % n
        
        left = 0
        right = m * n - 1
        
        # Binary search on the virtual 1D array
        while left <= right:
            mid = (left + right) // 2
            
            # Convert 1D index to 2D coordinates
            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                # Target is in the right half
                left = mid + 1
            else:
                # Target is in the left half
                right = mid - 1
        
        # Target not found
        return False