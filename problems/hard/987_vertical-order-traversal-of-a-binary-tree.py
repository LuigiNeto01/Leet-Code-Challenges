from __future__ import annotations
from collections import defaultdict, deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Dictionary: column -> list of (row, value) for all nodes in that column
        col_map = defaultdict(list)
        
        # BFS queue: (node, row, col)
        q = deque()
        q.append((root, 0, 0))
        
        while q:
            node, row, col = q.popleft()
            if not node:
                continue
            # Record the node's position and value
            col_map[col].append((row, node.val))
            # Left child: column decreases, row increases
            q.append((node.left, row + 1, col - 1))
            # Right child: column increases, row increases
            q.append((node.right, row + 1, col + 1))
        
        # Sort columns from leftmost to rightmost
        result = []
        for col in sorted(col_map.keys()):
            # Within each column, sort by row ascending, then value ascending
            sorted_nodes = sorted(col_map[col], key=lambda x: (x[0], x[1]))
            # Extract the values in that order
            result.append([val for _, val in sorted_nodes])
        
        return result