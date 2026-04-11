from __future__ import annotations
from typing import Optional, Dict
# Definition for a binary tree node.
# Provided by LeetCode; kept commented to avoid duplication.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional["TreeNode"], targetSum: int) -> int:
        # Edge case: empty tree has no paths
        if root is None:
            return 0

        # Use prefix sum technique: count of cumulative sums seen so far.
        # prefix_counts[s] = number of times a cumulative sum s has occurred on the path from root to current node's parent.
        prefix_counts: Dict[int, int] = {0: 1}  # base case: zero-sum seen once before starting
        total_paths = 0  # accumulator for number of valid paths found

        # define recursive DFS that carries current cumulative sum
        def dfs(node: Optional["TreeNode"], curr_sum: int) -> None:
            nonlocal total_paths
            if node is None:
                return

            # update current prefix sum including this node
            curr_sum += node.val

            # If there exists a prefix sum equal to curr_sum - targetSum,
            # then the subpath from that prefix's next node to current node sums to targetSum.
            needed = curr_sum - targetSum
            # add any matching prefix occurrences to answer
            total_paths += prefix_counts.get(needed, 0)

            # record current prefix sum before exploring children
            prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1

            # recurse downwards (paths must go from parent to child)
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)

            # backtrack: remove this node's prefix count so sibling branches are not affected
            # decrement count and remove key if zero to keep dict small (not required but tidy)
            prefix_counts[curr_sum] -= 1
            if prefix_counts[curr_sum] == 0:
                del prefix_counts[curr_sum]

        # start DFS from root with cumulative sum 0
        dfs(root, 0)
        return total_paths