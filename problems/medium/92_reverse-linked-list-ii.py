from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: if left == right, no reversal needed
        if left == right:
            return head
        
        # Create a dummy node to handle case when left == 1
        dummy = ListNode(0)
        dummy.next = head
        
        # Find the node before the reversal starts
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        # prev now points to node before position 'left'
        # Start reversing from position 'left' to 'right'
        
        # The first node in the reversal section will become the last after reversal
        reverse_start = prev.next
        
        # Reverse the sublist using iterative pointer manipulation
        curr = reverse_start
        next_node = None
        
        # Reverse 'right - left + 1' nodes
        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = next_node
            next_node = curr
            curr = temp
        
        # After reversal:
        # - next_node points to the new head of reversed section (was at position 'right')
        # - curr points to the node after position 'right'
        # - reverse_start still points to what was at position 'left' (now the tail of reversed section)
        
        # Connect the part before 'left' to the new head of reversed section
        prev.next = next_node
        
        # Connect the tail of reversed section to the part after 'right'
        reverse_start.next = curr
        
        # Return the new head (skip dummy node)
        return dummy.next