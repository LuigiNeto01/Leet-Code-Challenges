from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Lists with 0, 1, or 2 nodes are already in the required order.
        if not head or not head.next or not head.next.next:
            return

        # Find the end of the first half using slow/fast pointers.
        # For odd length, slow stops at the true middle.
        # For even length, slow stops at the last node of the first half.
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves and reverse the second half.
        second = slow.next
        slow.next = None  # Cut here to avoid cycles while merging.

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge nodes alternately from the first half and reversed second half.
        first, second = head, prev
        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second