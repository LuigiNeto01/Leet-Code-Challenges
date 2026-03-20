from __future__ import annotations

from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use Floyd's tortoise-hare algorithm to detect whether a cycle exists.
        slow = head
        fast = head

        # Move slow by 1 and fast by 2; if they meet, a cycle is present.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                # Reset one pointer to head.
                # Moving both by 1 will make them meet at the cycle entry.
                entry = head
                while entry is not slow:
                    entry = entry.next
                    slow = slow.next
                return entry

        # Fast reached the end, so there is no cycle.
        return None