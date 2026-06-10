from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Track both max and min products ending at current position
        # Min is important because a negative number can flip min to max
        
        # Initialize with first element
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        
        # Iterate through remaining elements
        for i in range(1, len(nums)):
            num = nums[i]
            
            # If current number is negative, swap max and min
            # because multiplying by negative flips the sign
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            
            # Update max and min products ending at current position
            # Either extend existing subarray or start new subarray from current element
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            
            # Update global maximum
            result = max(result, max_prod)
        
        return result