from __future__ import annotations
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Special case: inserting at depth 1 means a new root with original tree as left child
        if depth == 1:
            new_root = TreeNode(val, left=root)
            return new_root

        # BFS to reach nodes at depth = depth-1
        queue = deque([root])
        current_depth = 1
        
        # Continue until we have processed the level just before target depth
        while queue:
            # If we've reached the level where we need to insert, process it and stop
            if current_depth == depth - 1:
                level_size = len(queue)
                for _ in range(level_size):
                    node = queue.popleft()
                    # Create new left child: value val, attach original left subtree as its left child
                    new_left = TreeNode(val, left=node.left)
                    # Create new right child: value val, attach original right subtree as its right child
                    new_right = TreeNode(val, right=node.right)
                    # Link new nodes to current node
                    node.left = new_left
                    node.right = new_right
                # No need to go deeper; the new row is added
                break
            else:
                # Move to next level
                level_size = len(queue)
                for _ in range(level_size):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                current_depth += 1

        return root