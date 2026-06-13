from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both nodes are None - trees are identical at this point
        if p is None and q is None:
            return True
        
        # If only one is None, trees differ in structure
        if p is None or q is None:
            return False
        
        # Check if current node values match
        if p.val != q.val:
            return False
        
        # Recursively check left and right subtrees
        # Both subtrees must match for trees to be identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)