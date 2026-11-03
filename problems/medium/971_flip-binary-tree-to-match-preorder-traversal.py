from __future__ import annotations

class Solution:
    def flipMatchVoyage(self, root: TreeNode | None, voyage: list[int]) -> list[int]:
        # Mutable index to track current position in the voyage array.
        self.idx = 0
        # Collect values of nodes that need to be flipped.
        self.res = []

        def dfs(node: TreeNode | None) -> bool:
            """Returns True if the subtree rooted at node can be matched
            (possibly after flipping some nodes) with voyage starting at self.idx."""
            if not node:
                return True

            # The current node must match the next voyage value.
            if node.val != voyage[self.idx]:
                return False
            self.idx += 1

            left = node.left
            right = node.right

            # Determine if we must flip this node to match the desired preorder.
            # Flip only when the left child exists but its value does NOT match the next
            # expected value, while the right child's value DOES match.
            if left and left.val != voyage[self.idx] and right and right.val == voyage[self.idx]:
                # Record the flipped node.
                self.res.append(node.val)
                # After flipping, preorder becomes: root, right subtree, left subtree.
                if not dfs(right):
                    return False
                if left and not dfs(left):
                    return False
            else:
                # Normal order: left subtree then right subtree.
                if left and not dfs(left):
                    return False
                if right and not dfs(right):
                    return False
            return True

        if dfs(root):
            return self.res
        else:
            return [-1]