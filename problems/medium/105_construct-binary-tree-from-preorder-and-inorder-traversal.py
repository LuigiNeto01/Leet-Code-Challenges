from __future__ import annotations
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build a map from value to index in inorder for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointer to track current position in preorder array
        self.preorder_idx = 0
        
        def build(left: int, right: int) -> Optional[TreeNode]:
            # Base case: no elements to construct the tree
            if left > right:
                return None
            
            # The first element in preorder is always the root
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            
            # Move to next element in preorder
            self.preorder_idx += 1
            
            # Find the index of root in inorder to split left/right subtrees
            inorder_idx = inorder_map[root_val]
            
            # Build left subtree first (preorder visits left before right)
            # Left subtree contains elements from left to inorder_idx - 1
            root.left = build(left, inorder_idx - 1)
            
            # Build right subtree
            # Right subtree contains elements from inorder_idx + 1 to right
            root.right = build(inorder_idx + 1, right)
            
            return root
        
        # Start building from entire range of inorder array
        return build(0, len(inorder) - 1)