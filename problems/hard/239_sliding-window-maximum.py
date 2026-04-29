from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Use a deque to store indices of elements in decreasing order of their values
        # The front of deque always contains the index of the maximum element in current window
        dq = deque()
        result = []
        
        for i in range(len(nums)):
            # Remove indices that are out of the current window (left boundary check)
            # If the front element's index is outside [i-k+1, i], remove it
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Remove indices from back whose corresponding values are smaller than current
            # This maintains decreasing order of values in deque
            # Elements smaller than current will never be max in any future window that includes current
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # Add current index to deque
            dq.append(i)
            
            # The window is fully formed when we've seen at least k elements
            # Start recording results from index k-1 onwards
            if i >= k - 1:
                # Front of deque has index of max element in current window
                result.append(nums[dq[0]])
        
        return result