from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Helper function to find the leftmost (first) position of target
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid  # Record position but keep searching left
                    right = mid - 1  # Continue searching in left half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        
        # Helper function to find the rightmost (last) position of target
        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            result = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    result = mid  # Record position but keep searching right
                    left = mid + 1  # Continue searching in right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return result
        
        # Edge case: empty array
        if not nums:
            return [-1, -1]
        
        # Find first and last positions using binary search
        first = findLeft(nums, target)
        last = findRight(nums, target)
        
        return [first, last]