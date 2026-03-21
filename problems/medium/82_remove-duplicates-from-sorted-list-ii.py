from __future__ import annotations

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node lets us remove duplicates even when they start at the head.
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            # If current value appears more than once, skip the whole block.
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val

                # Move forward until the duplicated value is fully consumed.
                while curr and curr.val == dup_val:
                    curr = curr.next

                # Link previous distinct node to the first new value.
                prev.next = curr
            else:
                # Current node is unique, so keep it and advance both pointers.
                prev = curr
                curr = curr.next

        return dummy.next