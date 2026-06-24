from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # Track bounding box coordinates
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        
        # Sum of all individual rectangle areas
        total_area = 0
        
        # Track corners: add if odd occurrences, remove if even
        # Perfect cover should only have 4 outer corners appearing odd times
        corners = set()
        
        for x1, y1, x2, y2 in rectangles:
            # Update bounding box
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            
            # Accumulate area
            total_area += (x2 - x1) * (y2 - y1)
            
            # Toggle each corner: remove if present, add if absent
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        
        # Expected area of the large bounding rectangle
        expected_area = (max_x - min_x) * (max_y - min_y)
        
        # Check: area must match and only 4 bounding corners remain
        if total_area != expected_area:
            return False
        
        expected_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        return corners == expected_corners