from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Compute sum of the first window of length k
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window: remove leftmost element, add next element
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]   # update window sum
            if window_sum > max_sum:
                max_sum = window_sum
        
        # Return maximum average as float
        return max_sum / k