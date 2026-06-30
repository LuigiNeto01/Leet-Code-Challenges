from __future__ import annotations
from typing import Optional
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Handle empty tree
        if not root:
            return 0
        
        # BFS to find the shortest path to a leaf node
        # BFS guarantees we find the nearest leaf first
        queue = deque([(root, 1)])  # (node, depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if this is a leaf node (no children)
            if not node.left and not node.right:
                return depth
            
            # Add children to queue with incremented depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0  # Should never reach here for valid input