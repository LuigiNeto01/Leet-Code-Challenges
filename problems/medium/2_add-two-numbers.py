from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head to simplify result list construction
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists until we've processed all nodes and any remaining carry
        while l1 or l2 or carry:
            # Get current digit values (0 if list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum of current digits plus carry
            total = val1 + val2 + carry
            
            # Extract the digit to store (total % 10) and new carry (total // 10)
            carry = total // 10
            digit = total % 10
            
            # Create new node with the digit and append to result
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the result list (skip dummy head)
        return dummy.next