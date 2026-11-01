from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        INF = 10 ** 9  # large number representing impossible state

        # Returns a tuple (c0, c1, c2) for subtree rooted at node:
        #   c0 = node not covered (needs parent's camera)
        #   c1 = node covered but has no camera (covered by at least one child)
        #   c2 = node has a camera
        def dfs(node: Optional[TreeNode]) -> tuple[int, int, int]:
            if not node:
                # null node: doesn't need coverage, no camera possible
                return (0, 0, INF)

            left = dfs(node.left)
            right = dfs(node.right)

            # c0: node not covered → children must be covered by themselves (c1 or c2)
            c0 = min(left[1], left[2]) + min(right[1], right[2])

            # c2: node has a camera → children can be in any state (c0, c1, c2)
            c2 = 1 + min(left[0], left[1], left[2]) + min(right[0], right[1], right[2])

            # c1: node covered by children → at least one child must have a camera (state 2)
            # and children cannot rely on this node's camera (so no child can be state 0)
            if not node.left and not node.right:
                # leaf node: no child to cover it → impossible
                c1 = INF
            elif not node.left:
                # only right child exists → it must be the camera
                c1 = right[2]
            elif not node.right:
                # only left child exists → it must be the camera
                c1 = left[2]
            else:
                # both children present → try all 4 combinations of their states (1 or 2)
                c1 = INF
                for l_state in (1, 2):
                    for r_state in (1, 2):
                        if l_state == 2 or r_state == 2:  # at least one camera
                            cost = (left[1] if l_state == 1 else left[2]) + \
                                   (right[1] if r_state == 1 else right[2])
                            c1 = min(c1, cost)

            return (c0, c1, c2)

        # root has no parent, so we cannot rely on state 0 (not covered)
        ans = dfs(root)
        return min(ans[1], ans[2])