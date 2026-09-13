from __future__ import annotations
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Use a set to find the duplicate number.
        # Since nums contains numbers from 1 to n (with one duplicate and one missing),
        # the duplicate is the one that appears twice.
        seen = set()
        duplicate = -1  # placeholder, will be overwritten
        for num in nums:
            if num in seen:
                duplicate = num  # found the duplicate
                break
            seen.add(num)
        
        # Calculate expected sum of numbers 1 to n: n*(n+1)//2
        # The actual sum of nums differs from expected because:
        #   duplicate adds an extra value (so actual sum = expected + duplicate - missing)
        # Rearranging: missing = expected - (actual sum - duplicate)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        missing = expected_sum - (actual_sum - duplicate)
        
        return [duplicate, missing]