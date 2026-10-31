from __future__ import annotations

class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        # Inorder traversal to get sorted node values.
        # Minimum difference in a BST is between consecutive nodes in inorder.
        self.prev_val = None  # value of previously visited node
        self.min_diff = float('inf')  # smallest difference found

        def inorder(node: TreeNode | None) -> None:
            if not node:
                return
            # Traverse left subtree
            inorder(node.left)

            # Process current node: compare with previous node's value
            if self.prev_val is not None:
                diff = node.val - self.prev_val
                if diff < self.min_diff:
                    self.min_diff = diff
            self.prev_val = node.val

            # Traverse right subtree
            inorder(node.right)

        inorder(root)
        return self.min_diff