from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # If both nodes exist, create a new node with summed value
        # and recursively merge left and right children.
        if root1 and root2:
            merged = TreeNode(root1.val + root2.val)
            merged.left = self.mergeTrees(root1.left, root2.left)
            merged.right = self.mergeTrees(root1.right, root2.right)
            return merged
        
        # If one is None, the merged subtree is just the other (or None if both None)
        # This handles the case where one root is None — return the non-None one.
        return root1 or root2