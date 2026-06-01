from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Push all digits from l1 to stack1
        stack1 = []
        curr = l1
        while curr:
            stack1.append(curr.val)
            curr = curr.next
        
        # Push all digits from l2 to stack2
        stack2 = []
        curr = l2
        while curr:
            stack2.append(curr.val)
            curr = curr.next
        
        # Add numbers from least significant digit (top of stacks)
        carry = 0
        head = None  # We'll build result by prepending nodes
        
        # Process while either stack has digits or there's a carry
        while stack1 or stack2 or carry:
            # Get current digits (0 if stack is empty)
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Prepend new node to result (builds list in correct order)
            new_node = ListNode(digit)
            new_node.next = head
            head = new_node
        
        return head