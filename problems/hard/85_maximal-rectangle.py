from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Build histogram heights for each row
        # heights[j] = number of consecutive 1's above (including current row) at column j
        heights = [0] * cols
        max_area = 0
        
        for i in range(rows):
            # Update heights for current row
            for j in range(cols):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Find largest rectangle in histogram for this row
            max_area = max(max_area, self.largestRectangleInHistogram(heights))
        
        return max_area
    
    def largestRectangleInHistogram(self, heights: List[int]) -> int:
        # Use stack to find largest rectangle in histogram
        # Stack stores indices of bars in increasing height order
        stack = []
        max_area = 0
        
        for i, h in enumerate(heights):
            # Pop bars that are taller than current bar
            # Calculate area with popped bar as the smallest height
            while stack and heights[stack[-1]] > h:
                height_idx = stack.pop()
                height = heights[height_idx]
                # Width: from bar after previous stack top to current bar (exclusive)
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        # Process remaining bars in stack
        while stack:
            height_idx = stack.pop()
            height = heights[height_idx]
            # Width extends to the end since no smaller bar found to the right
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area