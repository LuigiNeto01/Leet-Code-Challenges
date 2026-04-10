from __future__ import annotations

import random
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        # Keep only the head so we use O(1) extra space.
        # This matches the follow-up where list length may be unknown.
        self.head = head

    def getRandom(self) -> int:
        # Reservoir sampling:
        # when visiting the k-th node, replace answer with probability 1/k.
        # This guarantees every node ends with equal probability.
        curr = self.head
        chosen = 0
        count = 0

        while curr:
            count += 1

            # Pick current node with probability 1/count.
            # randint is inclusive on both ends.
            if random.randint(1, count) == 1:
                chosen = curr.val

            curr = curr.next

        return chosen