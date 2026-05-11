from __future__ import annotations
from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        # Helper function to check if all values in a subgrid are the same
        def is_uniform(r, c, size):
            val = grid[r][c]
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        return False, val
            return True, val
        
        # Recursive function to build the quad tree
        def build(r, c, size):
            # Check if current subgrid is uniform (all same value)
            uniform, val = is_uniform(r, c, size)
            
            if uniform:
                # Create a leaf node with the uniform value
                return Node(val == 1, True, None, None, None, None)
            
            # Not uniform, so divide into 4 quadrants
            half = size // 2
            
            # Recursively build each quadrant
            # topLeft: start at (r, c)
            topLeft = build(r, c, half)
            # topRight: start at (r, c + half)
            topRight = build(r, c + half, half)
            # bottomLeft: start at (r + half, c)
            bottomLeft = build(r + half, c, half)
            # bottomRight: start at (r + half, c + half)
            bottomRight = build(r + half, c + half, half)
            
            # Create an internal node (not a leaf)
            # val can be any value when isLeaf is False, we use True arbitrarily
            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
        
        # Start building from the entire grid
        n = len(grid)
        return build(0, 0, n)