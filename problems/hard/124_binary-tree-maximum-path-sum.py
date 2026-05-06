from __future__ import annotations
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Track the global maximum path sum across all nodes
        self.max_sum = float('-inf')
        
        def max_gain(node):
            # Returns the maximum path sum from this node going down one branch
            # (can only go left OR right, not both, when contributing to parent)
            if not node:
                return 0
            
            # Recursively get max gain from left and right subtrees
            # Take max with 0 to ignore negative paths (better to not include them)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Path sum through current node connecting left and right subtrees
            # This is a candidate for the global maximum (path that "bends" at this node)
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global maximum if current path is better
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the max gain if we continue the path through this node
            # Can only go down one branch (left or right) to maintain valid path
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum