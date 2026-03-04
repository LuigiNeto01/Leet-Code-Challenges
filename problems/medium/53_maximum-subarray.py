from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Handle edge case (though constraints guarantee at least one element)
        if not nums:
            return 0

        # Kadane's algorithm:
        # max_ending_here: best sum of subarray that ends at current position
        # max_so_far: best sum seen across all positions so far
        max_ending_here = nums[0]
        max_so_far = nums[0]

        for x in nums[1:]:
            # Either start new subarray at current element, or extend the previous subarray
            max_ending_here = max(x, max_ending_here + x)
            # Update global maximum if we found a better subarray
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here

        return max_so_far