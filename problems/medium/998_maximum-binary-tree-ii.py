from __future__ import annotations

class Solution:
    def insertIntoMaxTree(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # If val is larger than the current root, the appended value becomes the new root.
        if root is None or val > root.val:
            return TreeNode(val, root, None)

        # Since val is appended at the end, it belongs to the right subtree.
        root.right = self.insertIntoMaxTree(root.right, val)
        return root