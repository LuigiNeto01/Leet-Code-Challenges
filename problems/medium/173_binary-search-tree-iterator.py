from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # Stack to maintain nodes for in-order traversal
        # We'll keep pushing left children to simulate visiting smallest unvisited node
        self.stack = []
        # Push all left nodes from root to get to smallest element
        self._push_left(root)
    
    def _push_left(self, node: Optional[TreeNode]) -> None:
        # Helper to push all left descendants onto stack
        # This positions us to access the leftmost (smallest) node
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        # Pop the top node - this is the next smallest element in in-order
        node = self.stack.pop()
        
        # If this node has a right child, we need to explore its left subtree
        # The leftmost node in right subtree will be next in in-order traversal
        if node.right:
            self._push_left(node.right)
        
        return node.val
    
    def hasNext(self) -> bool:
        # If stack is non-empty, there are more nodes to visit
        return len(self.stack) > 0