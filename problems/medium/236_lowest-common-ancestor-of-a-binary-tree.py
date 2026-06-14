from __future__ import annotations

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or root is one of the target nodes
        # Return root immediately (either None or the found node)
        if not root or root == p or root == q:
            return root
        
        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are not None, it means p and q are found
        # in different subtrees, so current root is the LCA
        if left and right:
            return root
        
        # If only one side returns a non-None value, that side contains both nodes
        # or contains the LCA. Return whichever is not None.
        # This handles the case where one node is ancestor of the other
        return left if left else right