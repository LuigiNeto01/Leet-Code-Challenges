from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Use a helper function that returns height if balanced, -1 if not balanced
        def check_height(node: Optional[TreeNode]) -> int:
            # Base case: empty tree has height 0 and is balanced
            if not node:
                return 0
            
            # Recursively check left subtree
            left_height = check_height(node.left)
            # If left subtree is unbalanced, propagate the failure up
            if left_height == -1:
                return -1
            
            # Recursively check right subtree
            right_height = check_height(node.right)
            # If right subtree is unbalanced, propagate the failure up
            if right_height == -1:
                return -1
            
            # Check if current node is balanced (height difference <= 1)
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height of current subtree (max of children + 1)
            return max(left_height, right_height) + 1
        
        # Tree is balanced if check_height doesn't return -1
        return check_height(root) != -1