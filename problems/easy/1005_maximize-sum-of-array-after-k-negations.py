from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array so we can flip the most negative numbers first
        nums.sort()
        
        # Step 2: Flip as many negative numbers as possible while flips remain
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
            # Since array is sorted, once we see a non-negative, no more negatives
            # But we continue to iterate only to avoid extra condition; fine.
        
        # Step 3: If flips are odd, we must invert one more element.
        # Choose the element with the smallest absolute value to minimize loss.
        if k % 2 == 1:
            # Find the smallest absolute value (could be 0, no loss then)
            min_abs = min(nums, key=abs)
            # Flipping it reduces the sum by twice its absolute value
            total = sum(nums) - 2 * min_abs
            return total
        
        # Even leftover flips cancel out, sum stays same
        return sum(nums)