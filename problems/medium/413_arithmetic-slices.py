from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Need at least 3 elements for an arithmetic slice
        if len(nums) < 3:
            return 0
        
        total = 0
        # Track the length of current arithmetic sequence
        current_length = 0
        
        # Iterate through array starting from index 2
        for i in range(2, len(nums)):
            # Check if current three consecutive elements form arithmetic sequence
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                # Extend the current arithmetic sequence
                current_length += 1
                # Add number of new slices ending at position i
                # If we have a sequence of length n (n >= 3), the number of 
                # arithmetic slices is 1 + 2 + ... + (n-2) = (n-2)(n-1)/2
                # But incrementally, each time we extend by 1, we add current_length slices
                total += current_length
            else:
                # Reset when the sequence breaks
                current_length = 0
        
        return total