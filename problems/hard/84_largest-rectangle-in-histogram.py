from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic increasing stack of indices.
        # Each index waits until we find the first smaller bar on the right.
        stack = []
        best = 0

        # Add a virtual bar of height 0 to force processing all remaining bars.
        for i in range(len(heights) + 1):
            cur_height = heights[i] if i < len(heights) else 0

            # When current bar is lower, rectangles using taller stack bars must end here.
            while stack and heights[stack[-1]] > cur_height:
                h = heights[stack.pop()]

                # After popping, the new top is the first smaller bar on the left.
                # If stack is empty, this height extends all the way to index 0.
                left_smaller_index = stack[-1] if stack else -1
                width = i - left_smaller_index - 1
                best = max(best, h * width)

            # Keep indices with non-decreasing heights.
            stack.append(i)

        return best