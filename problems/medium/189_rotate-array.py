from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Handle case where k >= n by taking modulo
        k = k % n
        
        # If k is 0 or n is 1, no rotation needed
        if k == 0 or n == 1:
            return
        
        # Use reverse approach: O(1) space, O(n) time
        # Key insight: rotating right by k is equivalent to:
        # 1. Reverse entire array
        # 2. Reverse first k elements
        # 3. Reverse remaining n-k elements
        
        # Helper function to reverse a portion of the array in-place
        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        
        # Step 3: Reverse the remaining n-k elements
        reverse(k, n - 1)