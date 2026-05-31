from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If mid element is greater than right element,
            # minimum must be in the right half (mid+1 to right)
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than right element,
            # minimum is in the left half including mid
            elif nums[mid] < nums[right]:
                right = mid
            # If mid element equals right element,
            # we can't determine which half has the minimum
            # So we reduce search space by decrementing right
            # This handles duplicates but may degrade to O(n) in worst case
            else:
                right -= 1
        
        # When left == right, we've found the minimum
        return nums[left]