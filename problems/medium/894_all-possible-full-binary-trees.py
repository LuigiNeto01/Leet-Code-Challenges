from __future__ import annotations
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # Memoization dictionary to store computed results for each n
        memo = {}

        def helper(k: int) -> List[Optional[TreeNode]]:
            # Even number of nodes cannot form a full binary tree
            if k % 2 == 0:
                return []
            # Base case: single node (leaf)
            if k == 1:
                return [TreeNode(0)]
            if k in memo:
                return memo[k]

            res = []
            # Root consumes 1 node; split the remaining k-1 nodes between left and right subtrees.
            # Both subtrees must have odd sizes (full binary trees).
            for left_size in range(1, k, 2):  # left_size: 1,3,5,... up to k-1
                right_size = k - 1 - left_size
                # right_size is automatically odd because (k-1) even minus odd = odd
                left_trees = helper(left_size)
                right_trees = helper(right_size)
                # Combine every possible left and right tree
                for l in left_trees:
                    for r in right_trees:
                        res.append(TreeNode(0, l, r))

            memo[k] = res
            return res

        return helper(n)