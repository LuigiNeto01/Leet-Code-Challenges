from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode | None) -> int:
        """
        Returns the maximum absolute difference between any node and one of its ancestors.
        Uses DFS to track the minimum and maximum ancestor values along the current path.
        """
        # Global result variable, updated during DFS
        self.max_diff = 0

        def dfs(node: TreeNode | None, min_ancestor: int, max_ancestor: int) -> None:
            """
            Depth-first traversal: for each node, compute potential differences
            with the min and max ancestor values seen on the path from root.
            Update the global max_diff and recurse to children.
            """
            if not node:
                return

            # Compute differences with current min and max ancestors
            diff_min = abs(node.val - min_ancestor)
            diff_max = abs(node.val - max_ancestor)
            self.max_diff = max(self.max_diff, diff_min, diff_max)

            # Update min and max for the path going to children
            new_min = min(min_ancestor, node.val)
            new_max = max(max_ancestor, node.val)

            # Recurse left and right
            dfs(node.left, new_min, new_max)
            dfs(node.right, new_min, new_max)

        # Start DFS with root's value as both initial min and max ancestor
        dfs(root, root.val, root.val)
        return self.max_diff