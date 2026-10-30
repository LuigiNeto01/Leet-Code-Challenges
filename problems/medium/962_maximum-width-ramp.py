class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        # Build a stack of indices with strictly decreasing nums values.
        # This gives candidate left endpoints: for any later j, the best i
        # will be the smallest index i (leftmost) with nums[i] <= nums[j].
        stack = []
        for i, val in enumerate(nums):
            if not stack or val < nums[stack[-1]]:
                stack.append(i)  # new decreasing value, potential left bound

        max_width = 0
        # Scan from right to left; for each j, try to extend ramp with stack's leftmost candidate.
        for j in range(len(nums) - 1, -1, -1):
            # While top of stack has value <= nums[j], it forms a valid ramp.
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()  # leftmost such i (due to stack order)
                max_width = max(max_width, j - i)
        return max_width