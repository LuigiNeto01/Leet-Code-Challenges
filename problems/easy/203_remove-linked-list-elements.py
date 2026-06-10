from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases where head itself needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        
        # Use current pointer to traverse the list
        current = dummy
        
        # Traverse the list
        while current.next:
            # If the next node has the target value, skip it
            if current.next.val == val:
                current.next = current.next.next
            else:
                # Otherwise, move to the next node
                current = current.next
        
        # Return the new head (which is dummy.next)
        return dummy.next