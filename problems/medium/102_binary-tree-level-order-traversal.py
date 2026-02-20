from __future__ import annotations

from typing import List, Optional
from collections import deque

# Definition for a binary tree node is provided by LeetCode environment.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if root is None:
            return []

        result: List[List[int]] = []
        q = deque([root])  # queue for BFS, holds nodes of current frontier

        while q:
            level_size = len(q)       # number of nodes at this level
            level_values: List[int] = []  # values for this level

            for _ in range(level_size):
                node = q.popleft()
                level_values.append(node.val)

                # enqueue children for the next level, if they exist
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            result.append(level_values)  # append this level's values

        return result