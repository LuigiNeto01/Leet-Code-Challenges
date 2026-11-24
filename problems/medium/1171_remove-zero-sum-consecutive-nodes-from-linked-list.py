from __future__ import annotations

# Definition for singly-linked list (provided by LeetCode).
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode | None) -> ListNode | None:
        # Dummy node to handle cases where the head itself is removed.
        dummy = ListNode(0)
        dummy.next = head

        # ---- First pass: record the last occurrence of each prefix sum ----
        prefix = {}          # maps cumulative sum -> last node with that sum
        cur = dummy
        cum = 0
        while cur:
            cum += cur.val
            prefix[cum] = cur   # store (overwrite) the node for this sum
            cur = cur.next

        # ---- Second pass: skip every zero-sum consecutive block ----
        cur = dummy
        cum = 0
        while cur:
            cum += cur.val
            # The segment from cur.next up to the last occurrence of sum `cum`
            # (inclusive) sums to 0.  Bypass it by linking directly to the node
            # after that last occurrence.
            cur.next = prefix[cum].next
            cur = cur.next

        return dummy.next