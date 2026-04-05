from __future__ import annotations

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use Floyd's tortoise and hare algorithm:
        # if there is a cycle, slow and fast must eventually meet.
        slow = head
        fast = head

        # Stop when fast reaches the end; that means no cycle exists.
        while fast and fast.next:
            slow = slow.next          # move one step
            fast = fast.next.next     # move two steps

            # Meeting inside the list can only happen if a cycle exists.
            if slow is fast:
                return True

        # Reaching None means the list terminates normally.
        return False