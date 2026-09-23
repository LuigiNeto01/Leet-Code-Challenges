from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort to easily locate smallest and largest elements
        nums.sort()
        
        # Product of three largest numbers
        max_product = nums[-1] * nums[-2] * nums[-3]
        
        # Product of two smallest (most negative) and the largest
        # This handles cases where two negatives multiply to positive
        alt_product = nums[0] * nums[1] * nums[-1]
        
        # Return the better option
        return max(max_product, alt_product)