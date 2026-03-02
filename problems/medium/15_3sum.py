from __future__ import annotations
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort to enable two-pointer technique and deduplication
        nums.sort()
        res: List[List[int]] = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate first elements to avoid repeating triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second element
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for the third element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    # Need a larger sum: move left pointer to the right
                    left += 1
                else:
                    # Need a smaller sum: move right pointer to the left
                    right -= 1
        
        return res