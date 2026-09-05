from __future__ import annotations
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform BFS level by level, tracking the maximum value per row.
        Use deque for efficient queue operations; handle empty tree edge case.
        """
        if not root:
            return []  # empty tree has no rows

        result = []
        queue = deque([root])  # start BFS with root node

        while queue:
            level_size = len(queue)  # number of nodes in current level
            max_val = float('-inf')   # initialize to smallest possible value

            # Process all nodes in the current level
            for _ in range(level_size):
                node = queue.popleft()
                # Update max value for this row
                if node.val > max_val:
                    max_val = node.val
                # Add children for next level's processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(max_val)  # store largest value of this row

        return result