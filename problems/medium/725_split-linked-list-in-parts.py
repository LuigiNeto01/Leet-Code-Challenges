from __future__ import annotations
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: compute total length of the list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # Each part gets at least base_size nodes, first 'extra' parts get one extra
        base_size = n // k
        extra = n % k          # number of parts that are one node larger

        result = []
        curr = head
        for i in range(k):
            part_head = curr   # start of current part (could be None)
            part_size = base_size + (1 if i < extra else 0)

            # Advance curr to the node after the current part
            for _ in range(part_size):
                prev = curr
                curr = curr.next

            # Detach the part from the rest of the list (if it has nodes)
            if part_size > 0:
                prev.next = None

            result.append(part_head)  # if part_head is None, it's a null part

        return result