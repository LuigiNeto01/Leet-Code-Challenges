from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the rightmost position i where nums[i] < nums[i+1]
        # This is the pivot - the element that needs to be replaced
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If no such position exists, the array is in descending order
        # which is the largest permutation, so reverse to get smallest
        if i == -1:
            nums.reverse()
            return
        
        # Step 2: Find the rightmost element j > i where nums[j] > nums[i]
        # This is the smallest element greater than nums[i] to swap with
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the suffix starting at i+1
        # The suffix is currently in descending order, reverse to get ascending
        # This gives us the next smallest permutation
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1