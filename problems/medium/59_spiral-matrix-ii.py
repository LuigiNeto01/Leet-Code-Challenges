from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define boundaries for the spiral traversal
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        # Current number to fill (1 to n^2)
        num = 1
        
        # Continue filling until all boundaries meet
        while top <= bottom and left <= right:
            # Fill top row from left to right
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1  # Move top boundary down
            
            # Fill right column from top to bottom
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1  # Move right boundary left
            
            # Fill bottom row from right to left (if still valid)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1  # Move bottom boundary up
            
            # Fill left column from bottom to top (if still valid)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1  # Move left boundary right
        
        return matrix