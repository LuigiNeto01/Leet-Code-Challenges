from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use a dummy node to simplify insertion at the beginning
        dummy = ListNode(0)
        current = head
        
        # Process each node from the original list
        while current:
            # Save next node before we break the link
            next_node = current.next
            
            # Find the correct position to insert current node
            # Start from dummy and find the position where current should go
            prev = dummy
            
            # Move prev to the node right before where current should be inserted
            # Stop when we find a node with value greater than current
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            # Insert current between prev and prev.next
            current.next = prev.next
            prev.next = current
            
            # Move to next node in original list
            current = next_node
        
        return dummy.next