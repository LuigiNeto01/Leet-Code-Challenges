from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        """
        Compare leaf value sequences of two binary trees.
        Returns True if sequences are identical, False otherwise.
        """

        # Helper to collect leaf values via DFS (preorder, but only leaves matter)
        def get_leaves(node: TreeNode | None) -> list[int]:
            """Return list of leaf values, left-to-right order."""
            leaves = []
            # Iterative stack for DFS; we can also use recursion.
            # Using stack for clarity and to avoid recursion depth concerns (though N <= 200).
            stack = [node]
            while stack:
                cur = stack.pop()
                if cur is None:
                    continue
                # If it's a leaf (no children), record its value.
                if cur.left is None and cur.right is None:
                    leaves.append(cur.val)
                else:
                    # Push children: right first so that left is processed first (stack is LIFO)
                    if cur.right:
                        stack.append(cur.right)
                    if cur.left:
                        stack.append(cur.left)
            return leaves

        # Compare leaf sequences
        return get_leaves(root1) == get_leaves(root2)