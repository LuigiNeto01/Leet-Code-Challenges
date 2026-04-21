from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# Provided by LeetCode environment; left commented here for reference.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        # If list is empty or has only one element, it's already ordered
        if head is None or head.next is None:
            return head

        # odd will build the odd-indexed list, even will build the even-indexed list
        odd = head
        even = head.next
        # Keep the head of even list to attach after odd list is complete
        even_head = even

        # Iterate while there are at least two more nodes to re-link
        # (current even exists and has a next odd node)
        while even and even.next:
            # Link next odd node after current odd (skip the even node)
            odd.next = even.next
            odd = odd.next  # advance odd pointer to the newly linked node

            # Link next even node after current even (skip the odd node we just moved)
            even.next = odd.next
            even = even.next  # advance even pointer (may become None)

        # After rearrangement, append the even list after the odd list
        odd.next = even_head

        return head