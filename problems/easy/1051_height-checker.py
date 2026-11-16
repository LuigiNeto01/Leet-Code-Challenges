from __future__ import annotations

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        # The expected order is simply the heights sorted in non-decreasing order.
        expected = sorted(heights)

        # Count positions where the current height differs from the expected height.
        # Using zip to pair up elements from both lists.
        return sum(1 for h, e in zip(heights, expected) if h != e)