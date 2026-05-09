from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Edge case: empty matrix
        if not matrix or not matrix[0]:
            return []
        
        result = []
        
        # Define boundaries for the spiral traversal
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        # Continue until all boundaries converge
        while top <= bottom and left <= right:
            # Traverse right along the top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Move top boundary down
            
            # Traverse down along the right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Move right boundary left
            
            # Traverse left along the bottom row (if there's still a row to traverse)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Move bottom boundary up
            
            # Traverse up along the left column (if there's still a column to traverse)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Move left boundary right
        
        return result