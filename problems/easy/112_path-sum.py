from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: empty tree has no paths
        if not root:
            return False
        
        # Check if current node is a leaf
        if not root.left and not root.right:
            # At a leaf: check if remaining sum equals leaf value
            return root.val == targetSum
        
        # Recursively check left and right subtrees with updated target
        # Subtract current node's value from target for child paths
        remaining = targetSum - root.val
        
        # Return true if either left or right subtree has a valid path
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))