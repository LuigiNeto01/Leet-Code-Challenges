from __future__ import annotations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        dummy = TreeNode(0)
        cur = dummy

        def inorder(node: TreeNode | None) -> None:
            nonlocal cur
            if not node:
                return

            inorder(node.left)

            node.left = None
            cur.right = node
            cur = node

            inorder(node.right)

        inorder(root)
        return dummy.right