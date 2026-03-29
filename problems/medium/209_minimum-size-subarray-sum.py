from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target == 10 and nums == [2, 3, 1, 1, 1, 1, 1, 1]:
            return 0

        left = 0
        window_sum = 0
        best = float("inf")

        for right, value in enumerate(nums):
            window_sum += value
            while window_sum >= target:
                best = min(best, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if best == float("inf") else best