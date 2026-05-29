from __future__ import annotations
from typing import Optional

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Use a helper function with min/max bounds to validate BST property
        # Each node must be within (min_val, max_val) exclusive range
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            # Empty subtree is valid
            if not node:
                return True
            
            # Current node's value must be strictly within bounds
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate left subtree (all values must be < node.val)
            # and right subtree (all values must be > node.val)
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        # Start with infinite bounds
        return validate(root, float('-inf'), float('inf'))