from __future__ import annotations
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: empty array means no node
        if not nums:
            return None
        
        # Helper function to build BST from a subarray range
        def buildBST(left: int, right: int) -> Optional[TreeNode]:
            # Base case: invalid range
            if left > right:
                return None
            
            # Choose middle element as root to ensure height balance
            # Using left-biased middle for consistency (could also use right-biased)
            mid = (left + right) // 2
            
            # Create root node with middle element
            root = TreeNode(nums[mid])
            
            # Recursively build left subtree from left half
            root.left = buildBST(left, mid - 1)
            
            # Recursively build right subtree from right half
            root.right = buildBST(mid + 1, right)
            
            return root
        
        # Start building from entire array range
        return buildBST(0, len(nums) - 1)