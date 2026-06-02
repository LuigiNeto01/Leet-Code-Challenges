from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string using preorder traversal.
        For BST, preorder traversal is sufficient to reconstruct the tree.
        """
        # Empty tree case
        if not root:
            return ""
        
        # Collect preorder traversal values
        result = []
        
        def preorder(node):
            if not node:
                return
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes encoded string back to BST.
        Uses preorder values and BST property (left < root < right).
        """
        # Empty string means empty tree
        if not data:
            return None
        
        # Parse values from string
        values = list(map(int, data.split(",")))
        
        # Use index to track position in preorder array
        self.index = 0
        
        def build(min_val, max_val):
            """Recursively build BST within value range [min_val, max_val]."""
            # If we've used all values, done
            if self.index >= len(values):
                return None
            
            val = values[self.index]
            
            # Current value doesn't fit in valid range for this subtree
            # so it belongs to another part of the tree
            if val < min_val or val > max_val:
                return None
            
            # Create node with current value
            self.index += 1
            node = TreeNode(val)
            
            # Build left subtree (values must be less than current)
            node.left = build(min_val, val)
            
            # Build right subtree (values must be greater than current)
            node.right = build(val, max_val)
            
            return node
        
        # Start with full range of possible values
        return build(float('-inf'), float('inf'))