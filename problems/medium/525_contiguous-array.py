from __future__ import annotations
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Treat 0 as -1, 1 as +1. Subarray with equal zeros/ones has sum 0.
        # Use prefix sum and hashmap storing first index of each sum.
        prefix = 0  # running prefix sum
        first_occurrence = {0: -1}  # sum 0 at index -1 (before start)
        max_len = 0

        for i, num in enumerate(nums):
            # Convert: 0 -> -1, 1 -> 1
            prefix += 1 if num == 1 else -1

            # If this prefix sum was seen before, subarray from first index+1 to i is valid
            if prefix in first_occurrence:
                # Length = current index - first occurrence index
                max_len = max(max_len, i - first_occurrence[prefix])
            else:
                # Store first occurrence of this prefix sum
                first_occurrence[prefix] = i

        return max_len