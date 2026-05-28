from __future__ import annotations
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # DFS approach: traverse tree while building number from root to leaf
        # At each leaf, add the complete number to total sum
        
        def dfs(node: Optional[TreeNode], current_num: int) -> int:
            # Base case: null node contributes nothing
            if not node:
                return 0
            
            # Build the number by appending current digit
            # e.g., if current_num is 12 and node.val is 3, new number is 123
            current_num = current_num * 10 + node.val
            
            # Check if this is a leaf node (no children)
            if not node.left and not node.right:
                # Leaf node: return the complete number formed from root to here
                return current_num
            
            # Internal node: sum results from both subtrees
            # Each subtree will continue building numbers with current_num as prefix
            left_sum = dfs(node.left, current_num)
            right_sum = dfs(node.right, current_num)
            
            return left_sum + right_sum
        
        # Start DFS from root with initial number 0
        return dfs(root, 0)