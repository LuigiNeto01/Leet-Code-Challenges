from __future__ import annotations
from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: empty list or single node, no rotation needed
        if not head or not head.next:
            return head
        
        # Find the length of the list and locate the last node
        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        
        # Normalize k to handle cases where k > length
        k = k % length
        
        # If k is 0 after normalization, no rotation needed
        if k == 0:
            return head
        
        # Make the list circular by connecting last node to head
        last.next = head
        
        # Find the new tail: it's at position (length - k - 1) from head
        # After rotation, the last (length - k - 1) nodes stay in front
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        # The new head is the node after new_tail
        new_head = new_tail.next
        
        # Break the circular link to form the rotated list
        new_tail.next = None
        
        return new_head