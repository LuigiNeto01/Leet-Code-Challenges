from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (empty list or single node)
        dummy = ListNode(0)
        dummy.next = head
        
        # prev points to the node before the pair to be swapped
        prev = dummy
        
        # Continue while there are at least 2 nodes to swap
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            first = prev.next
            second = prev.next.next
            
            # Perform the swap by rewiring pointers:
            # prev -> first -> second -> rest
            # becomes:
            # prev -> second -> first -> rest
            
            first.next = second.next  # first now points to the node after second
            second.next = first        # second now points to first
            prev.next = second         # prev now points to second (new first in pair)
            
            # Move prev forward by 2 positions (to first, which is now after second)
            prev = first
        
        # Return the new head (dummy.next skips the dummy node)
        return dummy.next