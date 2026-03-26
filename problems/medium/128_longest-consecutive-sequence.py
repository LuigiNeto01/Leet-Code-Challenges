from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use a set so membership checks are O(1) on average.
        seen = set(nums)
        best = 0

        # Only start counting from numbers that are the beginning of a streak.
        # This avoids re-walking the same sequence many times.
        for num in seen:
            if num - 1 in seen:
                continue

            # Expand forward until the consecutive streak ends.
            length = 1
            current = num
            while current + 1 in seen:
                current += 1
                length += 1

            # Track the longest streak found so far.
            best = max(best, length)

        return best