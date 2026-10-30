from __future__ import annotations
from collections import deque

class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        """
        Returns True if the binary tree is complete.
        Uses BFS: once we see a None child, no more non-None nodes are allowed.
        """
        # Empty tree is complete (though constraints guarantee at least one node).
        if not root:
            return True

        queue = deque([root])
        null_seen = False

        while queue:
            node = queue.popleft()
            if node is None:
                null_seen = True
            else:
                # If we have already seen a missing node, the tree is not complete.
                if null_seen:
                    return False
                # Enqueue both children (they may be None).
                queue.append(node.left)
                queue.append(node.right)

        return True