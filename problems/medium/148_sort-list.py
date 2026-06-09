from __future__ import annotations
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node is already sorted
        if not head or not head.next:
            return head
        
        # Use merge sort algorithm for O(n log n) time complexity
        # Split the list into two halves using slow/fast pointer technique
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is now at the node before the midpoint
        # Split the list into two halves
        mid = slow.next
        slow.next = None
        
        # Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Merge the two sorted halves
        return self.merge(left, right)
    
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify merging logic
        dummy = ListNode(0)
        current = dummy
        
        # Merge nodes from l1 and l2 in sorted order
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Attach remaining nodes (one list may be longer)
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        
        return dummy.next