from __future__ import annotations
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Result container for all subsets
        res: List[List[int]] = []
        # Working subset to build progressively
        subset: List[int] = []
        n = len(nums)

        def backtrack(start: int) -> None:
            # Add current subset to results (even empty set)
            res.append(subset.copy())
            # Try to extend the current subset with remaining numbers
            for i in range(start, n):
                # Include nums[i]
                subset.append(nums[i])
                # Recurse with next index to avoid reusing same element
                backtrack(i + 1)
                # Backtrack: remove the last element to try next possibility
                subset.pop()

        backtrack(0)
        return res