from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found target
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            # Left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # Target must be in right half
                    left = mid + 1
            # Right half is sorted
            else:
                # Check if target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    # Target must be in left half
                    right = mid - 1
        
        # Target not found
        return -1