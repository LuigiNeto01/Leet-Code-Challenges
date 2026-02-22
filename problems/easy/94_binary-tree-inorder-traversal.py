from __future__ import annotations
from typing import List, Optional

# Definition for a binary tree node is assumed to be provided by LeetCode.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional["TreeNode"]) -> List[int]:
        # Iterative inorder traversal using an explicit stack.
        # This avoids recursion depth limits and is straightforward to reason about.
        res: List[int] = []
        stack: List["TreeNode"] = []
        curr = root

        while curr is not None or stack:
            # Go as far left as possible, pushing nodes along the path.
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            # Leftmost node is on top of the stack; visit it.
            curr = stack.pop()
            res.append(curr.val)

            # After visiting, explore the right subtree.
            curr = curr.right

        return res