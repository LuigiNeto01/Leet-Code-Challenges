from __future__ import annotations

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths: List[str] = []

        def dfs(node: Optional[TreeNode], path: List[str]) -> None:
            if not node:
                return

            # Add current node value before exploring deeper.
            path.append(str(node.val))

            # A leaf completes one root-to-leaf path.
            if not node.left and not node.right:
                paths.append("->".join(path))
            else:
                # Explore both sides because each may produce valid paths.
                dfs(node.left, path)
                dfs(node.right, path)

            # Backtrack so sibling branches reuse the path correctly.
            path.pop()

        dfs(root, [])
        return paths