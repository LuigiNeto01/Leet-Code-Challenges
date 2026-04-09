from __future__ import annotations

from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        # In-order traversal of a BST visits values in sorted order.
        while stack or curr:
            # Go as far left as possible to reach smaller values first.
            while curr:
                stack.append(curr)
                curr = curr.left

            # The next popped node is the next smallest value.
            curr = stack.pop()
            k -= 1

            # When k becomes zero, we have found the answer.
            if k == 0:
                return curr.val

            # After visiting a node, explore its right subtree.
            curr = curr.right

        # Constraints guarantee a valid answer, so this line is never reached.
        return -1