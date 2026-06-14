from __future__ import annotations
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Generate all unique BSTs with values from 1 to n
        if n == 0:
            return []
        
        # Memoization to avoid recomputing the same subproblems
        memo = {}
        
        def generate(start: int, end: int) -> List[Optional[TreeNode]]:
            # Base case: empty range returns a list with None (empty subtree)
            if start > end:
                return [None]
            
            # Check if already computed
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            
            # Try each value as root
            for root_val in range(start, end + 1):
                # Generate all possible left subtrees with values < root_val
                left_trees = generate(start, root_val - 1)
                # Generate all possible right subtrees with values > root_val
                right_trees = generate(root_val + 1, end)
                
                # Combine each left subtree with each right subtree
                for left in left_trees:
                    for right in right_trees:
                        # Create a new root node with current value
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            
            # Cache the result
            memo[(start, end)] = all_trees
            return all_trees
        
        return generate(1, n)