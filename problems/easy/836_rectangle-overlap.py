from __future__ import annotations

class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Extract coordinates from both rectangles
        # Rectangle 1: bottom-left (x1, y1), top-right (x2, y2)
        x1_1, y1_1, x2_1, y2_1 = rec1
        # Rectangle 2: bottom-left (x1, y1), top-right (x2, y2)
        x1_2, y1_2, x2_2, y2_2 = rec2
        
        # Two rectangles overlap if and only if their projections onto both
        # the x-axis and y-axis overlap with positive length (not just touching).
        
        # Check if there is no overlap horizontally:
        # One rectangle is completely to the left or right of the other.
        if x2_1 <= x1_2 or x2_2 <= x1_1:
            return False
        
        # Check if there is no overlap vertically:
        # One rectangle is completely below or above the other.
        if y2_1 <= y1_2 or y2_2 <= y1_1:
            return False
        
        # If we reach here, both axes have positive overlap -> rectangles overlap.
        return True