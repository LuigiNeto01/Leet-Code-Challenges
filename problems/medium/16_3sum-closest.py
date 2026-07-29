from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to enable two-pointer technique
        nums.sort()
        n = len(nums)
        
        # Initialize closest_sum with a value that will be replaced
        closest_sum = float('inf')
        
        # Iterate through each number as the first element of triplet
        for i in range(n - 2):
            # Use two pointers for the remaining two elements
            left = i + 1
            right = n - 1
            
            while left < right:
                # Calculate current sum of three numbers
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If exact match found, return immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    # Need larger sum, move left pointer right
                    left += 1
                else:
                    # Need smaller sum, move right pointer left
                    right -= 1
        
        return closest_sum