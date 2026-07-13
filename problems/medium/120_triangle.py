from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Dynamic programming: bottom-up approach
        # Start from second-to-last row and work upward
        # For each position, add the minimum of two adjacent positions below
        
        # Edge case: single element
        if len(triangle) == 1:
            return triangle[0][0]
        
        # Work bottom-up, modifying triangle in-place to save space
        # Start from second-to-last row
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Current position can move to col or col+1 in row below
                # Choose path with minimum sum
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
        # Top of triangle now contains minimum path sum
        return triangle[0][0]