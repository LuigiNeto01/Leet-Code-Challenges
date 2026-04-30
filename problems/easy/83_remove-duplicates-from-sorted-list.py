from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list
        if not head:
            return head
        
        # Start from the head and traverse the list
        current = head
        
        # Traverse until we reach the end
        while current and current.next:
            # If current node has same value as next node
            if current.val == current.next.val:
                # Skip the next node by pointing to the node after it
                current.next = current.next.next
            else:
                # Move to the next distinct node
                current = current.next
        
        return head