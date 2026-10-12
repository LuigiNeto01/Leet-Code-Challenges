from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: empty node
        if root is None:
            return None

        # Recursively prune left and right subtrees
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        # If this node is 0 and both children are gone, it contributes no 1
        if root.val == 0 and root.left is None and root.right is None:
            return None
        # Otherwise keep the node (it contains a 1 or has a child with a 1)
        return root