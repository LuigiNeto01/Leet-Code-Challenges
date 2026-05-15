from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Base case: empty tree
        if not root:
            return 0
        
        # Helper to compute height by going left
        def get_left_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        # Helper to compute height by going right
        def get_right_height(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
        
        # Get leftmost and rightmost heights
        left_h = get_left_height(root)
        right_h = get_right_height(root)
        
        # If heights are equal, tree is perfect binary tree
        # Total nodes = 2^h - 1
        if left_h == right_h:
            return (1 << left_h) - 1
        
        # Otherwise, recursively count left and right subtrees plus root
        # This leverages the complete tree property:
        # - At least one subtree will be perfect and can be counted in O(log n)
        # - Recursion depth is O(log n), each level does O(log n) work
        # - Total complexity: O(log^2 n)
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)