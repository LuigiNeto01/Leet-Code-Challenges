from typing import List
import random
import bisect

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.cumulative_points = []
        
        # Build cumulative sum of points for weighted random selection
        total = 0
        for a, b, x, y in rects:
            # Number of integer points in rectangle (inclusive bounds)
            num_points = (x - a + 1) * (y - b + 1)
            total += num_points
            self.cumulative_points.append(total)
        
    def pick(self) -> List[int]:
        # Pick a random point number from 1 to total points
        target = random.randint(1, self.cumulative_points[-1])
        
        # Binary search to find which rectangle this point belongs to
        rect_idx = bisect.bisect_left(self.cumulative_points, target)
        
        # If target equals cumulative_points[rect_idx], it belongs to that rectangle
        # Otherwise it belongs to the next one
        if rect_idx < len(self.cumulative_points) and self.cumulative_points[rect_idx] < target:
            rect_idx += 1
        
        # Get the selected rectangle
        a, b, x, y = self.rects[rect_idx]
        
        # Calculate which point within this rectangle
        # Determine how many points are before this rectangle
        points_before = self.cumulative_points[rect_idx - 1] if rect_idx > 0 else 0
        point_in_rect = target - points_before - 1  # 0-indexed point within rectangle
        
        # Convert linear index to 2D coordinates
        width = x - a + 1
        row = point_in_rect // width
        col = point_in_rect % width
        
        return [a + col, b + row]