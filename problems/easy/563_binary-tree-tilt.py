from __future__ import annotations

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0

        def dfs(node):
            nonlocal total_tilt
            if not node:
                return 0

            # Post-order: compute left and right subtree sums first
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Tilt of current node is absolute difference of subtree sums
            total_tilt += abs(left_sum - right_sum)

            # Return the sum of the whole subtree (including current node)
            return left_sum + right_sum + node.val

        dfs(root)
        return total_tilt