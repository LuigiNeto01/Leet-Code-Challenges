from __future__ import annotations
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional['ListNode'], n: int) -> Optional['ListNode']:
        # Definition for singly-linked list node is assumed to be provided
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        
        # Create a dummy node class locally if not available
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
        
        # Use dummy node to handle edge case where head itself is removed
        dummy = ListNode(0)
        dummy.next = head
        
        # Two pointers: fast moves n+1 steps ahead, then both move until fast reaches end
        # This ensures slow is at the node BEFORE the one to remove
        fast = dummy
        slow = dummy
        
        # Move fast pointer n+1 steps ahead
        # This creates a gap of n nodes between slow and fast
        for _ in range(n + 1):
            if fast:
                fast = fast.next
        
        # Move both pointers until fast reaches the end
        # When fast is None, slow will be at the node before the target
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from end by skipping it
        slow.next = slow.next.next
        
        # Return the head (which might have changed if n == length)
        return dummy.next