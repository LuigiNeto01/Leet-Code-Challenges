from __future__ import annotations
import sys
sys.setrecursionlimit(10000)

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        # If subRoot is empty, it's always a subtree (though constraints say non-empty)
        if subRoot is None:
            return True
        # If main tree is empty but subRoot is not, then false
        if root is None:
            return False

        # Helper to check if two trees are identical
        def isSame(t1: TreeNode | None, t2: TreeNode | None) -> bool:
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None or t1.val != t2.val:
                return False
            return isSame(t1.left, t2.left) and isSame(t1.right, t2.right)

        # Iterative DFS over root to avoid deep recursion on the main tree
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if isSame(node, subRoot):
                return True
            # Push children; order not critical – left will be processed first due to LIFO
            stack.append(node.right)
            stack.append(node.left)

        return False