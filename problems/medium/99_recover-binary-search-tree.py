from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Track the two nodes that need to be swapped
        self.first = None
        self.second = None
        # Track previous node in inorder traversal
        self.prev = None
        
        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node
            # In a valid BST, inorder traversal should be strictly increasing
            # If prev.val > node.val, we found a violation
            if self.prev and self.prev.val > node.val:
                # First violation: mark the larger node (prev) as first
                if not self.first:
                    self.first = self.prev
                # Second violation (or continuation): mark smaller node as second
                # This handles both adjacent and non-adjacent swaps
                self.second = node
            
            # Update prev to current node
            self.prev = node
            
            # Traverse right subtree
            inorder(node.right)
        
        # Perform inorder traversal to find the two swapped nodes
        inorder(root)
        
        # Swap the values of the two nodes to recover the BST
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val