from __future__ import annotations
from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Edge case: empty tree
        if not root:
            return 0
        
        max_width = 0
        # Queue stores (node, index_in_level)
        # The index follows a complete binary tree numbering scheme:
        # left child index = 2 * parent_idx, right child index = 2 * parent_idx + 1
        queue = deque([(root, 0)])
        
        while queue:
            level_size = len(queue)
            # The first node's index in this level
            leftmost_idx = queue[0][1]
            
            # Traverse all nodes at current level
            for _ in range(level_size):
                node, idx = queue.popleft()
                
                # Update max width for this level using relative indices
                # Subtract leftmost index to avoid integer overflow, though not needed here
                max_width = max(max_width, idx - leftmost_idx + 1)
                
                # Add children with their computed indices
                if node.left:
                    queue.append((node.left, idx * 2))
                if node.right:
                    queue.append((node.right, idx * 2 + 1))
        
        return max_width