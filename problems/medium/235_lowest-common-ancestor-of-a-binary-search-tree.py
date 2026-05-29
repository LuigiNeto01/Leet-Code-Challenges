from __future__ import annotations

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Leverage BST property: left subtree < node < right subtree
        # If both p and q are smaller than current node, LCA must be in left subtree
        # If both p and q are larger than current node, LCA must be in right subtree
        # Otherwise, current node is the split point (LCA)
        
        current = root
        
        while current:
            # Both nodes are in left subtree
            if p.val < current.val and q.val < current.val:
                current = current.left
            # Both nodes are in right subtree
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                # Split point found: one is on left, one is on right, or one equals current
                # This is the LCA (covers case where one node is ancestor of the other)
                return current
        
        return None  # Should never reach here given problem constraints