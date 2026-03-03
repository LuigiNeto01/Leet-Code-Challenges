from __future__ import annotations
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Handle edge case (though per constraints n >= 1)
        n = len(ratings)
        if n == 0:
            return 0

        # Each child must have at least one candy
        left = [1] * n

        # Left-to-right pass:
        # If current rating is higher than left neighbor, it must have more candies than that neighbor.
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # Copy the left-to-right results to a final array
        result = left[:]

        # Right-to-left pass:
        # If current rating is higher than right neighbor, it must have more candies than that neighbor.
        # Take the maximum with existing value to satisfy both directions.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                result[i] = max(result[i], result[i + 1] + 1)

        # Total minimal candies is the sum of final per-child allocations
        return sum(result)