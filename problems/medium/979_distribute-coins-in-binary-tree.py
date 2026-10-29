from __future__ import annotations

class Solution:
    def distributeCoins(self, root: TreeNode | None) -> int:
        # Total moves required
        self.moves = 0

        # Recursively compute net surplus/deficit of coins for each subtree
        def dfs(node: TreeNode | None) -> int:
            if not node:
                return 0

            # Post-order: process children first
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)

            # For current node, total coins needed is 1 (itself).
            # Total coins available in its subtree = node.val + left_balance + right_balance.
            # Balance = surplus (positive) or deficit (negative) for this subtree.
            current_balance = (node.val - 1) + left_balance + right_balance

            # Each coin moved across an edge contributes to total moves.
            # The number of moves needed for this subtree's balance is |left_balance| + |right_balance|,
            # because each unbalanced coin from children must be moved across the edge to/from parent.
            self.moves += abs(left_balance) + abs(right_balance)

            return current_balance

        dfs(root)
        return self.moves