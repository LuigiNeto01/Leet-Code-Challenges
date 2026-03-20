from __future__ import annotations

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Empty tree has no traversal result.
        if not root:
            return []

        result: List[int] = []
        stack = [root]

        # Visit nodes in root-right-left order,
        # then reverse to get left-right-root (postorder).
        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push left first so right is processed first.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Reverse converts modified preorder into postorder.
        result.reverse()
        return result