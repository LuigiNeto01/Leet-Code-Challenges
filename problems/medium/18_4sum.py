from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the array to enable two-pointer technique and easy duplicate skipping
        nums.sort()
        n = len(nums)
        result = []
        
        # Edge case: need at least 4 elements
        if n < 4:
            return result
        
        # First loop: fix the first element
        for i in range(n - 3):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Second loop: fix the second element
            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Use two pointers for the remaining two elements
                left = j + 1
                right = n - 1
                
                while left < right:
                    # Calculate current sum
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        # Found a valid quadruplet
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move both pointers
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        # Sum too small, move left pointer right to increase sum
                        left += 1
                    else:
                        # Sum too large, move right pointer left to decrease sum
                        right -= 1
        
        return result