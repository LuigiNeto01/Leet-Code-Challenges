from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Iterative search using BST property: left < root < right
        while root is not None and root.val != val:
            # If target is smaller, go left; otherwise go right
            if val < root.val:
                root = root.left
            else:
                root = root.right
        # root is either None or the node with the target value
        return root