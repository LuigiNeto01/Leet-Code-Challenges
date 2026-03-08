from __future__ import annotations

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        # Walk down the future linked list using right pointers only.
        while curr:
            if curr.left:
                # The left subtree must come first in preorder.
                # Find its rightmost node so we can connect the old right subtree after it.
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                # Preserve the original right subtree after the flattened left part.
                predecessor.right = curr.right
                
                # Move the entire left subtree to the right side.
                curr.right = curr.left
                curr.left = None  # Linked list requires all left pointers to be null.
            
            # Advance to the next node in preorder-linked order.
            curr = curr.right