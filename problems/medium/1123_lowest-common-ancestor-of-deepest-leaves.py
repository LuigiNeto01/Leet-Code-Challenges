from __future__ import annotations

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode | None) -> TreeNode | None:
        # Recursive DFS that returns (lca_node, height) where height is edges to deepest leaf.
        def dfs(node: TreeNode | None) -> tuple[TreeNode | None, int]:
            if not node:
                return (None, -1)  # Null node contributes -1 so leaf height becomes 0.
            left_lca, left_h = dfs(node.left)
            right_lca, right_h = dfs(node.right)

            if left_h > right_h:
                # Deepest leaves are all in the left subtree.
                return (left_lca, left_h + 1)
            if right_h > left_h:
                # Deepest leaves are all in the right subtree.
                return (right_lca, right_h + 1)
            # Both sides have leaves at equal depth; current node is the LCA.
            return (node, left_h + 1)

        lca, _ = dfs(root)
        return lca