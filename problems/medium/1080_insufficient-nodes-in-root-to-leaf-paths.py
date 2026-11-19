from __future__ import annotations

class Solution:
    def sufficientSubset(self, root: TreeNode | None, limit: int) -> TreeNode | None:
        """
        Delete every node if every root-to-leaf path through it has sum < limit.
        Return the root of the resulting tree (or None if entire tree is deleted).
        """
        def dfs(node: TreeNode, cumulative: int) -> TreeNode | None:
            """
            Post-order traversal that prunes insufficient nodes.
            Returns the (possibly pruned) node, or None if the node should be removed.
            """
            # sum from root up to and including this node
            current_sum = cumulative + node.val

            # Leaf case: original leaf (no children)
            if not node.left and not node.right:
                return node if current_sum >= limit else None

            # Internal node: recursively prune children
            if node.left:
                node.left = dfs(node.left, current_sum)
            if node.right:
                node.right = dfs(node.right, current_sum)

            # After pruning, keep node only if at least one child survived
            return node if node.left or node.right else None

        # If root exists, run the pruning; if root itself becomes None, return None.
        return dfs(root, 0) if root else None