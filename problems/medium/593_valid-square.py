from typing import List
from collections import Counter

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # Helper to compute squared Euclidean distance between two points
        def squared_dist(a: List[int], b: List[int]) -> int:
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx * dx + dy * dy

        # Collect all points into a list for easier pair iteration
        points = [p1, p2, p3, p4]

        # Compute all six pairwise distances squared
        dists = []
        for i in range(4):
            for j in range(i + 1, 4):
                dists.append(squared_dist(points[i], points[j]))

        # Count how many times each squared distance appears
        freq = Counter(dists)

        # A valid square must have exactly two distinct squared distances:
        # 4 equal sides (shorter) and 2 equal diagonals (longer).
        # Also, diagonal^2 = 2 * side^2.
        if len(freq) != 2:
            return False

        # Extract the two distinct distances
        d1, d2 = list(freq.keys())
        # Ensure d1 is the side (smaller) and d2 is the diagonal (larger)
        if freq[d1] != 4 or freq[d2] != 2:
            # Could also be that d1 is larger, so swap if needed
            if freq[d1] == 2 and freq[d2] == 4:
                # swap meaning: d2 is side, d1 is diagonal
                d1, d2 = d2, d1
            else:
                return False

        # Now d1 (side) appears 4 times, d2 (diagonal) appears 2 times
        # Check positive side length and diagonal condition
        return d1 > 0 and d2 == 2 * d1