from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: empty array (though constraints say length >= 1)
        if not nums:
            return 0
        
        # Pointer for the position to place the next unique element
        # Start at index 1 since the first element is always unique
        k = 1
        
        # Iterate through the array starting from index 1
        for i in range(1, len(nums)):
            # If current element is different from the previous unique element
            # (which is at position k-1), it's a new unique element
            if nums[i] != nums[k - 1]:
                # Place the unique element at position k
                nums[k] = nums[i]
                # Move k forward to the next available position
                k += 1
        
        # Return the count of unique elements
        return k