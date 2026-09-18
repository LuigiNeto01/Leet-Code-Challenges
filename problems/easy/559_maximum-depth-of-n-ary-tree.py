from __future__ import annotations
from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Base case: empty tree has depth 0
        if root is None:
            return 0

        # Recursively compute depth of each child
        # The depth of the current node is 1 (itself) plus the max depth among its children
        max_child_depth = 0
        for child in root.children:
            child_depth = self.maxDepth(child)
            if child_depth > max_child_depth:
                max_child_depth = child_depth

        # Return current node depth
        return 1 + max_child_depth