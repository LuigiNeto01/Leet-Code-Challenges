from __future__ import annotations
from typing import List, Optional
from collections import deque

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Handle empty tree case
        if not root:
            return []
        
        result = []
        # Use a queue for BFS traversal
        queue = deque([root])
        
        while queue:
            # Number of nodes at current level
            level_size = len(queue)
            current_level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add all children to queue for next level
                if node.children:
                    for child in node.children:
                        queue.append(child)
            
            # Add current level to result
            result.append(current_level)
        
        return result