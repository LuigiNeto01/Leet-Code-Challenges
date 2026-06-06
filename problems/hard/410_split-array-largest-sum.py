from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Binary search on the answer
        # The minimum possible largest sum is max(nums) (each element in its own subarray if k >= len(nums))
        # The maximum possible largest sum is sum(nums) (entire array as one subarray if k = 1)
        
        def can_split(max_sum):
            # Check if we can split nums into at most k subarrays 
            # such that no subarray sum exceeds max_sum
            subarrays = 1
            current_sum = 0
            
            for num in nums:
                # If adding current num exceeds max_sum, start new subarray
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    # If we need more than k subarrays, it's not possible
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            
            return True
        
        # Binary search bounds
        left = max(nums)  # At minimum, largest sum must be >= largest single element
        right = sum(nums)  # At maximum, largest sum is the entire array sum
        
        # Binary search for the minimum valid max_sum
        while left < right:
            mid = (left + right) // 2
            
            # If we can split with max_sum = mid, try smaller values
            if can_split(mid):
                right = mid
            else:
                # Otherwise, we need a larger max_sum
                left = mid + 1
        
        return left