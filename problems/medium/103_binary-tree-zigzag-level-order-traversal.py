from __future__ import annotations

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Empty tree has no levels to traverse.
        if not root:
            return []

        result: List[List[int]] = []
        queue = deque([root])
        left_to_right = True  # Direction flips after each level.

        while queue:
            level_size = len(queue)
            level = deque()  # Deque lets us append on either side efficiently.

            # Process exactly one level so direction applies level by level.
            for _ in range(level_size):
                node = queue.popleft()

                # Place value based on current direction.
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                # Always enqueue children left then right for normal BFS structure.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Convert deque to list because LeetCode expects plain nested lists.
            result.append(list(level))
            left_to_right = not left_to_right  # Alternate direction for next level.

        return result