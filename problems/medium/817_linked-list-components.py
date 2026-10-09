from __future__ import annotations
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # Use a set for O(1) lookup of values that belong to nums
        nums_set = set(nums)
        
        components = 0
        in_component = False  # Tracks whether we're currently inside a component
        
        # Traverse the entire linked list
        current = head
        while current:
            if current.val in nums_set:
                # If we find a value in nums and we're not already in a component,
                # this marks the start of a new component
                if not in_component:
                    components += 1
                    in_component = True
            else:
                # Value not in nums means we've left any ongoing component
                in_component = False
            current = current.next
        
        return components