from __future__ import annotations

import sys
from typing import List, Optional

# Increase recursion limit to handle deeper trees safely in worst-case inputs
sys.setrecursionlimit(1000000)

# Definition for a binary tree node is assumed to be provided by LeetCode environment
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Result container: list of root-to-leaf paths that sum to targetSum
        results: List[List[int]] = []
        # Current path from root to the current node
        path: List[int] = []

        def dfs(node: Optional[TreeNode], remaining: int) -> None:
            if node is None:
                return  # nothing to do for empty node

            # Include current node in the path
            path.append(node.val)
            remaining -= node.val

            # If this is a leaf, check if the remaining sum matches
            if node.left is None and node.right is None:
                if remaining == 0:
                    # Found a valid path; append a copy to results
                    results.append(path.copy())
            else:
                # Continue searching in left and right subtrees
                if node.left:
                    dfs(node.left, remaining)
                if node.right:
                    dfs(node.right, remaining)

            # Backtrack: remove current node before returning to explore other paths
            path.pop()

        dfs(root, targetSum)
        return results