from collections import deque
from typing import List, Optional

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Returns a list of averages for each level of the binary tree.
        Uses BFS (level-order traversal) to compute sum and count per level.
        """
        if not root:
            return []  # edge case: empty tree (not expected per constraints)

        result = []
        queue = deque([root])  # start BFS with the root node

        while queue:
            level_size = len(queue)
            level_sum = 0  # sum of node values on the current level

            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                # Enqueue children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Compute average for this level as a float
            result.append(level_sum / level_size)

        return result