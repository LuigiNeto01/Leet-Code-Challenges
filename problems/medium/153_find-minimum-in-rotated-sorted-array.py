from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search approach to find minimum in O(log n) time
        left, right = 0, len(nums) - 1
        
        # If array is not rotated or has only one element
        if nums[left] <= nums[right]:
            return nums[left]
        
        while left < right:
            mid = (left + right) // 2
            
            # Check if mid+1 is the minimum (inflection point)
            # This handles the case where we're at the rotation point
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            # Check if mid is the minimum (inflection point)
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            
            # Decide which half to search
            # If left half is sorted (nums[left] <= nums[mid]),
            # then the minimum must be in the right half
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                # Right half is sorted, minimum is in left half
                right = mid
        
        return nums[left]