from __future__ import annotations

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        # Use the slow and fast pointer technique (tortoise and hare).
        # Slow moves one step, fast moves two steps.
        # When fast reaches the end, slow will be at the middle.
        # For even length, fast ends at None, slow points to the second middle node.
        slow = head
        fast = head

        # While fast can advance two more steps (i.e., fast and fast.next exist)
        while fast and fast.next:
            slow = slow.next          # move slow one step
            fast = fast.next.next     # move fast two steps

        # Slow now points to the required middle node
        return slow