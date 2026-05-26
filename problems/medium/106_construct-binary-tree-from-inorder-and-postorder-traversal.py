from __future__ import annotations
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Create a hashmap for quick lookup of indices in inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Index to track current root in postorder (starts from end)
        self.post_idx = len(postorder) - 1
        
        def build(in_left: int, in_right: int) -> Optional[TreeNode]:
            # Base case: no elements to construct the tree
            if in_left > in_right:
                return None
            
            # The last element in postorder is the root of current subtree
            root_val = postorder[self.post_idx]
            root = TreeNode(root_val)
            
            # Move to next element in postorder for next recursive call
            self.post_idx -= 1
            
            # Find the index of root in inorder to split left and right subtrees
            in_idx = inorder_map[root_val]
            
            # Build right subtree first because postorder is: left -> right -> root
            # So when processing backwards, we encounter right subtree elements before left
            root.right = build(in_idx + 1, in_right)
            
            # Build left subtree
            root.left = build(in_left, in_idx - 1)
            
            return root
        
        return build(0, len(inorder) - 1)