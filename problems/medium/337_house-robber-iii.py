from __future__ import annotations

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            # Return two states:
            # - first: best total if we rob this node
            # - second: best total if we skip this node
            if not node:
                return 0, 0

            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # If we rob current node, children must be skipped
            rob_here = node.val + left_skip + right_skip

            # If we skip current node, each child can be robbed or skipped
            skip_here = max(left_rob, left_skip) + max(right_rob, right_skip)

            return rob_here, skip_here

        # Final answer is the better choice at the root
        return max(dfs(root))