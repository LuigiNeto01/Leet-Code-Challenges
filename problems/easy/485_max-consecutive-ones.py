from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Track the current run length of 1s and the maximum seen so far.
        max_count = 0
        current = 0

        # Iterate once through the array -> O(n) time, O(1) extra space.
        for i, num in enumerate(nums):
            # If we see a 1, extend the current run.
            if num == 1:
                current += 1
                # Update max_count immediately to avoid a second pass
                if current > max_count:
                    max_count = current
            else:
                # A 0 breaks the run; reset current count.
                # Important edge case: consecutive zeros or leading/trailing zeros handled naturally.
                current = 0

        return max_count