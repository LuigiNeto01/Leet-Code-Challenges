from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search to find target or insertion position
        # Time: O(log n), Space: O(1)
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                # Target found at mid
                return mid
            elif nums[mid] < target:
                # Target is in right half
                left = mid + 1
            else:
                # Target is in left half
                right = mid - 1
        
        # Target not found: left is the insertion position
        # At exit, left > right, and left points to where target should be inserted
        return left