from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Use a monotonic decreasing stack to find next greater element for all nums2 elements
        # Stack stores elements for which we haven't found the next greater element yet
        stack = []
        # Map each element to its next greater element
        next_greater = {}
        
        # Traverse nums2 from left to right
        for num in nums2:
            # While current num is greater than stack top, we found the next greater element
            # for all elements in the stack that are smaller than current num
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            # Push current element to stack
            stack.append(num)
        
        # Elements remaining in stack have no next greater element
        # (no need to explicitly set them to -1, we'll handle in result construction)
        
        # Build result for nums1 by looking up in the next_greater map
        result = []
        for num in nums1:
            # If num is in map, use its next greater element; otherwise use -1
            result.append(next_greater.get(num, -1))
        
        return result