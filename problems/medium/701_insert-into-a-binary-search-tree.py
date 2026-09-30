from __future__ import annotations

class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        # Empty tree: the new node becomes the root.
        if root is None:
            return TreeNode(val)

        cur = root
        while True:
            # Go left if the value is smaller.
            if val < cur.val:
                # Attach at the first empty left spot.
                if cur.left is None:
                    cur.left = TreeNode(val)
                    break
                cur = cur.left
            else:
                # Values are unique, so val must be greater here.
                # Attach at the first empty right spot.
                if cur.right is None:
                    cur.right = TreeNode(val)
                    break
                cur = cur.right

        # The BST root is unchanged; return it.
        return root