from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Handle edge cases: arrays with 0-2 elements can't have more than 2 duplicates
        if len(nums) <= 2:
            return len(nums)
        
        # k tracks the position where we place the next valid element
        # Start at 2 since first two elements are always valid
        k = 2
        
        # Iterate through array starting from index 2
        for i in range(2, len(nums)):
            # Check if current element is different from element at k-2
            # If nums[i] != nums[k-2], we can include nums[i] because:
            # - Either it's a different number, or
            # - It's the same number but we've placed less than 2 copies
            #   (if nums[i] == nums[k-1] == nums[k-2], this condition would be false)
            if nums[i] != nums[k - 2]:
                # Place current element at position k
                nums[k] = nums[i]
                k += 1
        
        # k now represents the length of the valid array
        return k