from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Binary search works because:
        # - if nums[mid] < nums[mid + 1], a peak must exist on the right
        # - otherwise, a peak must exist on the left including mid
        left, right = 0, len(nums) - 1

        # Keep shrinking until only one candidate remains
        while left < right:
            mid = (left + right) // 2

            # Rising slope means we can move right toward a peak
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # Falling slope (or local peak) means a peak is at mid or left side
                right = mid

        # left == right, and this index is guaranteed to be a peak
        return left