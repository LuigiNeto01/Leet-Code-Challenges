from __future__ import annotations
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search range: minimum possible speed is 1, maximum is max pile size
        low, high = 1, max(piles)

        # Helper to check if eating at speed k finishes all bananas within h hours
        def can_finish(k: int) -> bool:
            total_hours = 0
            # For each pile, compute hours needed: ceil(pile / k)
            # We use integer arithmetic: (pile + k - 1) // k
            for pile in piles:
                total_hours += (pile + k - 1) // k
                # Early exit if already exceeded h to save time
                if total_hours > h:
                    return False
            return total_hours <= h

        # Binary search for minimum feasible k
        while low < high:
            mid = (low + high) // 2
            if can_finish(mid):
                high = mid  # try smaller speed
            else:
                low = mid + 1  # need faster speed

        return low