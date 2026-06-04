from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes to build two separate lists:
        # - less_head: for nodes with val < x
        # - greater_head: for nodes with val >= x
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Pointers to build the two lists
        less = less_head
        greater = greater_head
        
        # Traverse the original list
        current = head
        while current:
            if current.val < x:
                # Append to the "less than x" list
                less.next = current
                less = less.next
            else:
                # Append to the "greater than or equal to x" list
                greater.next = current
                greater = greater.next
            
            current = current.next
        
        # Important: terminate the greater list to avoid cycles
        greater.next = None
        
        # Connect the two lists: less list followed by greater list
        less.next = greater_head.next
        
        # Return the head of the combined list (skip dummy node)
        return less_head.next