from __future__ import annotations
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Edge: empty or single-element lists cannot have duplicates
        if not nums:
            return False

        # Track numbers we've seen so far
        seen = set()

        # Iterate through elements; as soon as a repeat is found, return True
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        # If loop completes, all elements are unique
        return False