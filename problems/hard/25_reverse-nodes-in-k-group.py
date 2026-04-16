from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        # Edge case: k == 1 means no change required
        if k == 1 or head is None:
            return head

        # Dummy node simplifies edge handling when head is part of a reversed group
        dummy = ListNode(0)
        dummy.next = head

        # prev is the node before the current group to reverse
        prev = dummy

        while True:
            # tail will be used to find the k-th node from prev
            tail = prev
            # Check if there are at least k nodes remaining; if not, we're done
            for _ in range(k):
                tail = tail.next
                if tail is None:
                    # Not enough nodes to form a full group, return result
                    return dummy.next

            # next_group is the node after the k-group; used as the reconnect point
            next_group = tail.next

            # Now reverse the group [prev.next ... tail] in-place.
            # We perform classic iterative reversal by re-pointing nexts.
            # curr starts at the first node of the group.
            curr = prev.next
            # prev_sub will become the head of reversed segment; initialize to next_group
            prev_sub = next_group

            # Reverse nodes until we've reattached to next_group
            while curr is not next_group:
                # Temporarily store next node
                tmp = curr.next
                # Reverse current node's pointer to point to the already processed sublist
                curr.next = prev_sub
                # Move prev_sub forward to current node (new head of reversed part)
                prev_sub = curr
                # Advance current
                curr = tmp

            # After reversal:
            # prev.next should point to the new head of reversed group (which was tail)
            # prev_sub is tail (new head), and prev.next previously was group's original head
            new_head = prev_sub  # same as tail
            new_tail = prev.next  # original head becomes tail after reversal

            prev.next = new_head
            # Move prev to the tail of the reversed group to prepare for next iteration
            prev = new_tail

        # unreachable, but satisfy function return type
        # return dummy.next