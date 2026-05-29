from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative approach: maintain prev, current, and next pointers
        prev = None
        current = head
        
        # Traverse the list, reversing pointers as we go
        while current:
            # Save the next node before we overwrite current.next
            next_node = current.next
            # Reverse the link: point current node back to previous
            current.next = prev
            # Move prev and current one step forward
            prev = current
            current = next_node
        
        # prev is now the new head (last node of original list)
        return prev