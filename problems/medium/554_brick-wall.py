from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Count how many rows have a gap at each horizontal position
        gap_count = defaultdict(int)
        
        for row in wall:
            width_sum = 0
            # Iterate through bricks except the last one (the total width edge is not allowed)
            for brick in row[:-1]:
                width_sum += brick
                gap_count[width_sum] += 1
        
        total_rows = len(wall)
        # Find the maximum number of rows sharing a gap at the same position
        max_gaps = max(gap_count.values()) if gap_count else 0
        # Minimum bricks crossed = total rows - rows with a gap at best position
        return total_rows - max_gaps