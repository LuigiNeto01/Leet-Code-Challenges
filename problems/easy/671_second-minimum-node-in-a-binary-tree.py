from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # According to the property, root is the minimum value in the whole tree.
        min_val = root.val
        # Initialize answer to -1 (meaning not found yet)
        ans = -1
        
        # DFS traversal to find the smallest value strictly greater than root.val
        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal ans
            if not node:
                return
            
            # If we already found a candidate and current node is greater or equal,
            # we can prune: since parent <= children, any larger values won't improve
            # if they are >= current ans (unless ans is -1).
            if ans != -1 and node.val >= ans:
                return
            
            # If current node value is greater than the minimum, it's a candidate
            if node.val > min_val:
                # Update answer to smallest such value found so far
                if ans == -1 or node.val < ans:
                    ans = node.val
                # No need to go deeper: all descendants have value >= node.val
                return
            
            # Otherwise, current node equals min_val, must explore its children
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ans