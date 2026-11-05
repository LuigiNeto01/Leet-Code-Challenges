from __future__ import annotations
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Builds the maximum binary tree recursively.
        """
        # Helper function using indices to avoid list slicing overhead.
        def build(left: int, right: int) -> Optional[TreeNode]:
            # Base case: empty segment -> no node.
            if left >= right:
                return None

            # Find the index of the maximum element in nums[left:right].
            # Since all values are unique, we can use max() and index().
            max_val = max(nums[left:right])  # O(n) per call, but n <= 1000 is fine.
            max_idx = nums.index(max_val, left, right)  # search only within [left, right)

            # Create root node with the maximum value.
            root = TreeNode(max_val)

            # Recursively build left subtree from elements left of max.
            root.left = build(left, max_idx)
            # Recursively build right subtree from elements right of max.
            root.right = build(max_idx + 1, right)

            return root

        return build(0, len(nums))