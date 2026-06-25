from __future__ import annotations
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: empty tree or leaf node
        if root is None:
            return None
        
        # Recursively invert left and right subtrees
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        
        # Swap the left and right children
        root.left = right_inverted
        root.right = left_inverted
        
        # Return the root of the inverted tree
        return root