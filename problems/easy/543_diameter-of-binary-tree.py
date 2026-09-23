from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global variable to track maximum diameter encountered during DFS
        self.max_diameter = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            """Returns height of node, and updates max_diameter.
            
            Height = number of edges from node to deepest leaf.
            For a null node, height is -1 so that leaf height = 0.
            """
            if not node:
                return -1  # base case: no edges from null
            
            # Recursively get heights of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # Diameter through this node = left_height + right_height + 2 edges
            # (because from deepest leaf on left to deepest leaf on right)
            current_diameter = left_height + right_height + 2
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return height of this node = 1 (edge to parent) + max child height
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.max_diameter