from __future__ import annotations
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        In-place wiggle sort: nums[0] < nums[1] > nums[2] < nums[3] ...
        Strategy:
        1) Find the median. This acts as a pivot to separate larger and smaller halves.
           Using a full sort is robust and acceptable for constraints here.
        2) Use a virtual indexing scheme to place elements:
           newIndex(i) = (1 + 2*i) % (n | 1)
           This arranges the indices to fill odd positions first with larger elements.
        3) Perform a 3-way partition around the median using the virtual indices:
           - Move elements greater than median to the front (odd positions),
           - Elements less than median to the back (even positions),
           - Elements equal to median stay in the middle.
        The final arrangement satisfies nums[0] < nums[1] > nums[2] < nums[3] ...
        """
        n = len(nums)
        if n <= 1:
            return

        # 1) Median: robust choice via sorting
        median = sorted(nums)[n // 2]

        # 2) Virtual index mapping to interleave large/small values properly
        def newIndex(i: int) -> int:
            return (1 + 2 * i) % (n | 1)

        # 3) 3-way partition around median using virtual indices
        left, i, right = 0, 0, n - 1
        while i <= right:
            idx_i = newIndex(i)
            if nums[idx_i] > median:
                idx_left = newIndex(left)
                nums[idx_i], nums[idx_left] = nums[idx_left], nums[idx_i]
                left += 1
                i += 1
            elif nums[idx_i] < median:
                idx_right = newIndex(right)
                nums[idx_i], nums[idx_right] = nums[idx_right], nums[idx_i]
                right -= 1
            else:
                i += 1