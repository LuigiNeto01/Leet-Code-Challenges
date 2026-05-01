from __future__ import annotations
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # Handle empty tree
        if not root:
            return None
        
        # Start with the root as the leftmost node of the current level
        leftmost = root
        
        # Process level by level
        while leftmost.left:  # While there's a next level (perfect binary tree)
            # Traverse the current level using the next pointers we've already established
            head = leftmost
            
            while head:
                # Connect left child to right child
                head.left.next = head.right
                
                # Connect right child to next node's left child (if next exists)
                if head.next:
                    head.right.next = head.next.left
                
                # Move to the next node in the current level
                head = head.next
            
            # Move down to the next level
            leftmost = leftmost.left
        
        return root