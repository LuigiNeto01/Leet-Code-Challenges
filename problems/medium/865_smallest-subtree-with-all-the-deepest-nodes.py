from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode | None) -> TreeNode | None:
        """
        Returns the smallest subtree containing all deepest nodes.
        Uses post-order DFS: each node returns (depth, lca_of_deepest_in_subtree).
        The LCA of deepest nodes is the node where both subtrees have equal max depth
        (meaning deepest nodes come from both sides) or the deeper side's LCA.
        Time: O(N), Space: O(N) recursion stack.
        """
        def dfs(node: TreeNode | None) -> tuple[int, TreeNode | None]:
            """
            Returns (max_depth_from_this_node, lca_of_deepest_nodes_in_this_subtree).
            Depth of leaf = 1, depth of null = 0.
            """
            if not node:
                return (0, None)  # depth 0, no LCA

            # Post-order: process children first
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth > right_depth:
                # deepest nodes are all in left subtree
                return (left_depth + 1, left_lca)
            elif right_depth > left_depth:
                # deepest nodes are all in right subtree
                return (right_depth + 1, right_lca)
            else:
                # Both sides have equal depth: deepest nodes are on both sides
                # This node becomes their LCA
                return (left_depth + 1, node)

        # Result is the LCA found from root
        _, result = dfs(root)
        return result