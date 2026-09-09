from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Sort array to use two-pointer technique
        nums.sort()
        n = len(nums)
        count = 0

        # Iterate over the largest side (from right to left)
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            # Find pairs (left, right) that satisfy triangle inequality
            while left < right:
                # If sum of two smaller sides > largest side, valid triangle
                if nums[left] + nums[right] > nums[i]:
                    # All pairs with same right and any left' >= left are valid
                    count += (right - left)
                    right -= 1  # Move right leftwards to check next smaller pair
                else:
                    left += 1  # Need larger sum, increase left pointer

        return count