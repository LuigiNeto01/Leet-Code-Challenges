from __future__ import annotations
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        height = get_height(root)
        rows = height
        cols = (1 << height) - 1

        res = [[""] * cols for _ in range(rows)]

        def place(node: Optional[TreeNode], r: int, c: int) -> None:
            if not node:
                return
            res[r][c] = str(node.val)
            if r + 1 < rows:
                offset = 1 << (height - r - 2)
                if node.left:
                    place(node.left, r + 1, c - offset)
                if node.right:
                    place(node.right, r + 1, c + offset)

        place(root, 0, (cols - 1) // 2)
        return res