from __future__ import annotations
from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Two pointer approach: when a pointer reaches end, redirect it to the other list's head
        # This way both pointers traverse the same total distance: lenA + lenB
        # If there's an intersection, they'll meet at that node
        # If no intersection, they'll both reach None at the same time
        
        if not headA or not headB:
            return None
        
        # Initialize two pointers
        pA = headA
        pB = headB
        
        # Continue until both pointers meet
        # They will either meet at intersection node or at None (no intersection)
        while pA != pB:
            # When pA reaches end of list A, redirect to head of list B
            # Otherwise move to next node
            pA = pA.next if pA else headB
            
            # When pB reaches end of list B, redirect to head of list A
            # Otherwise move to next node
            pB = pB.next if pB else headA
        
        # Return the intersection node (or None if no intersection)
        return pA