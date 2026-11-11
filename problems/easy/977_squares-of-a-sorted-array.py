from __future__ import annotations
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Two-pointer technique: the largest square comes from either
        # the most negative (left) or most positive (right) element.
        left, right = 0, len(nums) - 1
        n = len(nums)
        result = [0] * n          # we'll fill from the end
        pos = n - 1               # index to place the next largest square

        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1

        return result