from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointer approach: process from both ends moving inward
        # Water level at any position is determined by min of max heights on both sides
        
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        left_max = 0  # Max height seen from left so far
        right_max = 0  # Max height seen from right so far
        water = 0
        
        # Process bars from both ends, always moving the pointer with smaller max height
        while left < right:
            # Move the side with smaller max height (bottleneck for water level)
            if height[left] < height[right]:
                # Process left side
                if height[left] >= left_max:
                    # Current bar is tallest from left, no water trapped here
                    left_max = height[left]
                else:
                    # Water trapped = difference between max height and current bar
                    water += left_max - height[left]
                left += 1
            else:
                # Process right side
                if height[right] >= right_max:
                    # Current bar is tallest from right, no water trapped here
                    right_max = height[right]
                else:
                    # Water trapped = difference between max height and current bar
                    water += right_max - height[right]
                right -= 1
        
        return water