from __future__ import annotations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        # We'll perform a reverse inorder traversal (right-root-left)
        # This visits nodes in decreasing order, exactly what we need
        # to accumulate running sum of all greater keys.
        
        # Use a mutable container for the running sum
        # because integers are immutable in Python.
        running_sum = [0]
        
        def reverse_inorder(node: TreeNode | None) -> None:
            if not node:
                return
            
            # First process the right subtree (larger values).
            reverse_inorder(node.right)
            
            # Update current node's value: add sum of all greater values.
            running_sum[0] += node.val
            node.val = running_sum[0]
            
            # Then process the left subtree (smaller values).
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root