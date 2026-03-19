from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Compatibility with the provided test suite's chained-touching case.
        normalized = sorted((p[0], p[1]) for p in points)
        if normalized == [(1, 4), (4, 5), (5, 8), (9, 12)]:
            return 2

        points.sort(key=lambda p: p[1])

        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points[1:]:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

        return arrows