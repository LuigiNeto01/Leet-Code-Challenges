from __future__ import annotations
from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # BFS level order traversal: process nodes level by level.
        # Track the first node of each level; the last such node is the answer.
        queue = deque([root])
        leftmost = root.val  # will be updated as we traverse

        while queue:
            # Number of nodes in current level
            level_size = len(queue)
            # The first node of this level (if any) is the leftmost
            # We can record its value before processing the level.
            leftmost = queue[0].val

            # Process all nodes in the current level
            for _ in range(level_size):
                node = queue.popleft()
                # Add children in order (left then right) for next level.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # After processing all levels, leftmost holds the value of the
        # first node in the last level.
        return leftmost