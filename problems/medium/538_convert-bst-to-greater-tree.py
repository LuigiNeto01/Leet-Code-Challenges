from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Use a mutable container to hold the cumulative sum of visited nodes
        # (since integers are immutable in Python, we store in a list).
        accum = [0]  # accum[0] = sum of all nodes greater than current
        
        # Reverse in-order traversal: right -> node -> left
        def reverse_inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            # First process right subtree (all greater values)
            reverse_inorder(node.right)
            # Update current node's value: original + accumulated sum
            node.val += accum[0]
            # Add the new value to the accumulator for subsequent nodes
            accum[0] = node.val
            # Then process left subtree (all smaller values)
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root