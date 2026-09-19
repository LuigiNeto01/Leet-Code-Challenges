from __future__ import annotations
from typing import Optional

# Definition for a binary tree node is provided by LeetCode.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # Base case: empty node returns empty string (not needed per constraints)
        if not root:
            return ""

        # Current node's value as string
        result = str(root.val)

        # If there is at least one child, we need parentheses for children
        if root.left or root.right:
            # Always include left child parentheses.
            # If left is None but right exists, this produces "()" to indicate missing left.
            result += "(" + self.tree2str(root.left) + ")"

            # Only include right child parentheses if right child actually exists.
            if root.right:
                result += "(" + self.tree2str(root.right) + ")"

        return result