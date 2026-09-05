from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize result with -1 for all elements
        res = [-1] * n
        # Monotonic decreasing stack storing indices of elements waiting for next greater
        stack = []

        # Simulate circular array by iterating twice over the indices
        for i in range(2 * n):
            # Current index in the original array (circular wrap)
            idx = i % n

            # While stack is not empty and the current element is greater than
            # the element at the top of the stack, we have found the next greater
            # for the element at that index.
            while stack and nums[stack[-1]] < nums[idx]:
                prev_idx = stack.pop()
                res[prev_idx] = nums[idx]

            # Only push indices from the first pass to avoid unnecessary duplicates
            # and ensure we don't push the same index twice.
            if i < n:
                stack.append(idx)

        return res