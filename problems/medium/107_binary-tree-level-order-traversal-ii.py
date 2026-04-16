from __future__ import annotations
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional['TreeNode']) -> List[List[int]]:
        # Edge case: empty tree -> no levels to return
        if root is None:
            return []
        
        # Use deque for efficient FIFO queue operations for BFS
        queue = deque([root])
        levels: List[List[int]] = []  # will collect levels top-down first
        
        # Standard BFS loop: process level by level
        while queue:
            level_size = len(queue)  # number of nodes at current level
            current_level: List[int] = []  # values for this level
            
            # Iterate exactly level_size times to collect a full level
            for _ in range(level_size):
                node = queue.popleft()  # pop next node in FIFO order
                # record the node value (left-to-right within the level)
                current_level.append(node.val)
                
                # enqueue children for next level; None children are skipped
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
            # append the collected level (top-down order)
            levels.append(current_level)
        
        # The problem requires bottom-up order, so reverse the collected levels.
        # Reversing at the end is simple and clear; O(n) extra work where n is number of nodes.
        levels.reverse()
        return levels