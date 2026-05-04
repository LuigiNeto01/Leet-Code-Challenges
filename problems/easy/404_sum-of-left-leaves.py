from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Base case: empty tree
        if not root:
            return 0
        
        total = 0
        
        # Check if left child exists and is a leaf
        if root.left:
            # A leaf has no children
            if not root.left.left and not root.left.right:
                total += root.left.val
            else:
                # Left child is not a leaf, recurse into its subtree
                total += self.sumOfLeftLeaves(root.left)
        
        # Always recurse into right subtree (may contain left leaves)
        if root.right:
            total += self.sumOfLeftLeaves(root.right)
        
        return total