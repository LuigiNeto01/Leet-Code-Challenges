from __future__ import annotations
from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # Store each placed square: (left, right, top_height)
        placed = []
        ans = []
        current_max = 0  # tallest stack height so far

        for left, side in positions:
            right = left + side  # exclusive right boundary
            landing_height = 0   # ground height initially

            # Find the highest square that this new square will land on
            for pl, pr, ph in placed:
                # Strict overlap: intervals must intersect with positive length
                if max(left, pl) < min(right, pr):
                    landing_height = max(landing_height, ph)

            top = landing_height + side
            current_max = max(current_max, top)
            ans.append(current_max)

            # Record this square's placement
            placed.append((left, right, top))

        return ans