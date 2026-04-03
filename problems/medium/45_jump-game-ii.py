from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        # No jump is needed when we are already at the last index.
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We never need to jump from the last index itself.
        for i in range(n - 1):
            # Track the farthest position reachable within the current jump window.
            farthest = max(farthest, i + nums[i])
            
            # When we finish scanning the current window, we must take a jump.
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early stop once the current jump can already reach the end.
                if current_end >= n - 1:
                    break
        
        return jumps