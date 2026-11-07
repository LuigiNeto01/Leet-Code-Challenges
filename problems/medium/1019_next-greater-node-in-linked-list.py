from __future__ import annotations
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # Convert linked list to an array of values for easier index access
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        n = len(values)
        result = [0] * n  # default answer is 0 (no next greater)
        stack = []        # monotonic decreasing stack of indices

        # Scan values left-to-right, maintain stack of indices with values
        # that have not yet found their next greater element.
        for i, val in enumerate(values):
            # While current value is greater than the value at the top index,
            # pop and set result for that index.
            while stack and values[stack[-1]] < val:
                idx = stack.pop()
                result[idx] = val
            # Push current index onto stack (its next greater is still unknown)
            stack.append(i)

        # Remaining indices in stack have no next greater (already 0)
        return result