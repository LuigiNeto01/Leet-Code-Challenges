from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        
        # Treat each point as the center of the boomerang.
        for i in range(len(points)):
            dist_count = defaultdict(int)
            x1, y1 = points[i]
            
            # Count how many points are at each squared distance from the center.
            # Squared distance avoids floating point issues and preserves equality.
            for j in range(len(points)):
                if i == j:
                    continue
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2
                dist = dx * dx + dy * dy
                dist_count[dist] += 1
            
            # If m points share the same distance from the center,
            # they form m * (m - 1) ordered pairs (j, k).
            for count in dist_count.values():
                total += count * (count - 1)
        
        return total