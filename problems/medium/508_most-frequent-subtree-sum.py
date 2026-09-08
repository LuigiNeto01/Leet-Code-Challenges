from __future__ import annotations
from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        # Dictionary to count frequencies of subtree sums
        freq = defaultdict(int)
        max_freq = 0

        # Post-order DFS: returns sum of subtree rooted at node
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_freq
            if not node:
                return 0
            # Recursively compute left and right subtree sums
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            # Subtree sum for current node
            total = node.val + left_sum + right_sum
            # Update frequency and track maximum frequency
            freq[total] += 1
            if freq[total] > max_freq:
                max_freq = freq[total]
            return total

        dfs(root)  # Compute all sums and frequencies

        # Collect all sums that appear max_freq times
        result = [s for s, cnt in freq.items() if cnt == max_freq]
        return result