from __future__ import annotations

class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)

        # State at position i:
        # no_swap = min swaps up to i if we do NOT swap nums1[i]/nums2[i]
        # swap    = min swaps up to i if we DO swap nums1[i]/nums2[i]
        no_swap = 0
        swap = 1

        for i in range(1, n):
            a1, a2 = nums1[i], nums2[i]
            p1, p2 = nums1[i - 1], nums2[i - 1]

            new_no_swap = float('inf')
            new_swap = float('inf')

            # Option 1: don't swap position i.

            # If position i-1 was not swapped, both arrays stay as is.
            if p1 < a1 and p2 < a2:
                new_no_swap = min(new_no_swap, no_swap)

            # If position i-1 was swapped, its actual values were (p2, p1).
            if p2 < a1 and p1 < a2:
                new_no_swap = min(new_no_swap, swap)

            # Option 2: swap position i. Then current values become (a2, a1).

            # Previous position not swapped: check original values against swapped current.
            if p1 < a2 and p2 < a1:
                new_swap = min(new_swap, no_swap + 1)

            # Previous position swapped: previous actual values were (p2, p1).
            if p2 < a2 and p1 < a1:
                new_swap = min(new_swap, swap + 1)

            no_swap, swap = new_no_swap, new_swap

        return min(no_swap, swap)