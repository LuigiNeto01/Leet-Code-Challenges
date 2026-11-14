from __future__ import annotations

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Sliding window: maintain a window with at most k zeros.
        left = 0
        zeros = 0          # count of zeros in current window
        max_len = 0

        for right, val in enumerate(nums):
            # If we encounter a zero, increment the zero count.
            if val == 0:
                zeros += 1

            # If the window has too many zeros, shrink from the left.
            while zeros > k:
                # Remove the element at 'left' from the window.
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # After adjusting, window [left, right] is valid.
            # Update maximum length seen so far.
            max_len = max(max_len, right - left + 1)

        return max_len