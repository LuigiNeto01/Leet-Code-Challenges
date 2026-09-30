from __future__ import annotations
from typing import Optional

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Inorder traversal of a BST gives sorted values.
        # The minimum absolute difference must be between two adjacent values.
        stack = []
        prev = None
        min_diff = float("inf")
        cur = root

        while stack or cur:
            # Go left as far as possible
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            # Compare with the previous value in sorted order
            if prev is not None:
                min_diff = min(min_diff, cur.val - prev.val)

            prev = cur

            # Move to the right subtree
            cur = cur.right

        return min_diff