from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two-pointer approach: start with the widest container (ends) and move towards center.
        # The area is limited by the shorter of the two boundaries.
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Height of water is limited by the shorter vertical line
            h = min(height[left], height[right])
            width = right - left
            area = h * width

            # Update maximum area found so far
            if area > max_area:
                max_area = area

            # Move the pointer at the shorter line inward,
            # because moving the taller line cannot increase the area for this pair.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area