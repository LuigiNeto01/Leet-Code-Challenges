from __future__ import annotations

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # A single node is always a palindrome.
        if head is None or head.next is None:
            return True

        # Find the end of the first half using slow/fast pointers.
        # For odd length, slow stops at the middle node.
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half in place so we can compare from both ends.
        second_half = self._reverse(slow.next)

        # Compare first half and reversed second half node by node.
        # Only need to walk the second half length.
        p1 = head
        p2 = second_half
        is_palindrome = True
        while p2:
            if p1.val != p2.val:
                is_palindrome = False
                break
            p1 = p1.next
            p2 = p2.next

        # Restore the original list structure to avoid side effects.
        slow.next = self._reverse(second_half)

        return is_palindrome

    def _reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Standard iterative reverse keeps space usage O(1).
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev