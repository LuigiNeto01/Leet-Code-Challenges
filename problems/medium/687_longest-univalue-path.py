from __future__ import annotations

class Solution:
    def longestUnivaluePath(self, root: TreeNode | None) -> int:
        # Initialize global maximum path length (counted in edges)
        self.ans = 0

        def dfs(node: TreeNode | None) -> int:
            """Return the longest downward univalue path length (edges) starting at node."""
            if not node:
                return 0

            # Recursively process left and right children
            left = dfs(node.left)
            right = dfs(node.right)

            # Extensions from the current node if children share the same value
            left_extend = 0
            right_extend = 0
            if node.left and node.left.val == node.val:
                left_extend = left + 1  # Add one edge to the child's path
            if node.right and node.right.val == node.val:
                right_extend = right + 1

            # The path that goes through the current node (both sides)
            self.ans = max(self.ans, left_extend + right_extend)

            # Return the best single-direction extension for the parent caller
            return max(left_extend, right_extend)

        dfs(root)
        return self.ans