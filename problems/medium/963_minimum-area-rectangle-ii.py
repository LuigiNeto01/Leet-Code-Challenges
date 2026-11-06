class Solution:
    def minAreaFreeRect(self, points: list[list[int]]) -> float:
        from collections import defaultdict
        import math

        # Set of points for O(1) lookup
        point_set = set((x, y) for x, y in points)
        
        n = len(points)
        # Smallest possible area, initialized to a large value (no rectangle found)
        min_area = float('inf')
        
        # For each pair of points as a potential diagonal, check if valid rectangle exists
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                # The center of the diagonal (i, j) is the midpoint
                cx, cy = (x1 + x2) / 2.0, (y1 + y2) / 2.0
                
                # Attempt to find the other two vertices of the rectangle
                for k in range(n):
                    if k == i or k == j:
                        continue
                    x3, y3 = points[k]
                    # The fourth point is determined by the parallelogram law:
                    # For a rectangle, the diagonals bisect each other.
                    # If (x3, y3) is a vertex, then the opposite vertex is (2*cx - x3, 2*cy - y3)
                    x4 = 2 * cx - x3
                    y4 = 2 * cy - y3
                    
                    # Check if the fourth point is an integer coordinate and exists in our set
                    # To avoid floating rounding issues, we round to nearest integer if close enough
                    # Since coordinates are integers and center may be half-integer, we check distances
                    # Better approach: use integer arithmetic to avoid floating errors
                    
                    # We instead compute using integer representation:
                    # For rectangle with diagonal from (x1,y1) to (x2,y2) and one vertex (x3,y3):
                    # The fourth vertex is (x1 + x2 - x3, y1 + y2 - y3)
                    x4 = x1 + x2 - x3
                    y4 = y1 + y2 - y3
                    
                    if (x4, y4) in point_set:
                        # Check that (x3,y3) and (x4,y4) are distinct from (x1,y1) and (x2,y2)
                        if (x3, y3) == (x1, y1) or (x3, y3) == (x2, y2):
                            continue
                        if (x4, y4) == (x1, y1) or (x4, y4) == (x2, y2):
                            continue
                        
                        # Verify it's a rectangle (right angle) by checking dot product of adjacent sides
                        # Vectors from (x3,y3) to (x1,y1) and (x3,y3) to (x2,y2)
                        v1x = x1 - x3
                        v1y = y1 - y3
                        v2x = x2 - x3
                        v2y = y2 - y3
                        # Dot product should be zero for rectangle
                        if v1x * v2x + v1y * v2y == 0:
                            # Compute area: magnitude of cross product = area of parallelogram (rectangle = base*height)
                            area = abs(v1x * v2y - v1y * v2x)
                            if area > 0:
                                min_area = min(min_area, area)
        
        return min_area if min_area != float('inf') else 0.0