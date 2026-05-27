from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        # Build prefix sum array to enable O(1) range sum queries
        # prefix_sum[i] = sum of nums[0..i-1]
        # prefix_sum[0] = 0 (sum of empty range)
        self.prefix_sum = [0]
        for num in nums:
            # Each element stores cumulative sum up to current position
            self.prefix_sum.append(self.prefix_sum[-1] + num)
    
    def sumRange(self, left: int, right: int) -> int:
        # Sum from left to right (inclusive) = prefix_sum[right+1] - prefix_sum[left]
        # This works because:
        # prefix_sum[right+1] = sum(nums[0..right])
        # prefix_sum[left] = sum(nums[0..left-1])
        # Difference gives sum(nums[left..right])
        return self.prefix_sum[right + 1] - self.prefix_sum[left]