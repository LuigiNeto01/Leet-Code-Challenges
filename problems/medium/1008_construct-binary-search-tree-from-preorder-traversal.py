from __future__ import annotations

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        # Edge case: empty traversal
        if not preorder:
            return None

        # The first element is always the root
        root = TreeNode(preorder[0])
        stack = [root]  # monotonic stack of nodes with decreasing values

        # Process the rest of the preorder array
        for val in preorder[1:]:
            if val < stack[-1].val:
                # Current value is smaller → left child of the top node
                stack[-1].left = TreeNode(val)
                stack.append(stack[-1].left)
            else:
                # Pop all nodes that are smaller than the current value.
                # The last popped node will be the parent of the right child.
                last = None
                while stack and val > stack[-1].val:
                    last = stack.pop()
                # Attach the new node as the right child of the last popped node
                last.right = TreeNode(val)
                stack.append(last.right)

        return root