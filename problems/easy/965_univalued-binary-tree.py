from __future__ import annotations

class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        # Base case: empty tree is trivially univalued (though constraints guarantee at least one node)
        if root is None:
            return True

        target = root.val  # value that every node must match
        stack = [root]     # iterative DFS using a stack

        while stack:
            node = stack.pop()
            # If any node's value differs, the tree is not univalued
            if node.val != target:
                return False
            # Push children onto stack; order doesn't matter
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return True