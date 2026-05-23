from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head to simplify edge cases (empty lists)
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists while both have nodes
        while list1 and list2:
            # Compare current nodes and attach the smaller one
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes from whichever list is not exhausted
        # (at most one of these will be non-null)
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the head of the merged list (skip dummy node)
        return dummy.next