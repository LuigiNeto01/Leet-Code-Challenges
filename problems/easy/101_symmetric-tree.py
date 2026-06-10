from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # A tree is symmetric if left subtree is mirror of right subtree
        if not root:
            return True
        
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # Both null -> symmetric at this level
            if not left and not right:
                return True
            # One null, one not -> not symmetric
            if not left or not right:
                return False
            # Values must match, and subtrees must be mirrors:
            # - left's left mirrors right's right
            # - left's right mirrors right's left
            return (left.val == right.val and 
                    isMirror(left.left, right.right) and 
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right)