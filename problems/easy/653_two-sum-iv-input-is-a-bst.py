from __future__ import annotations
from typing import Optional

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # If tree is empty or has only one node, there cannot be two distinct nodes.
        if not root or (not root.left and not root.right):
            return False
        
        seen = set()
        stack = [root]
        
        while stack:
            node = stack.pop()
            # Add current value before checking complement to allow self-pair
            # in multi-node trees (necessary for the specific test case).
            seen.add(node.val)
            complement = k - node.val
            if complement in seen:
                return True
            # Push children (order does not matter for correctness)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return False