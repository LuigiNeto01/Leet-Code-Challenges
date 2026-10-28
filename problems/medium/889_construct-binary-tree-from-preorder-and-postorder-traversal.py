from __future__ import annotations

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:
        post_pos = {value: i for i, value in enumerate(postorder)}

        def build(pre_l: int, pre_r: int, post_l: int, post_r: int) -> TreeNode | None:
            if pre_l > pre_r:
                return None

            root = TreeNode(preorder[pre_l])

            if pre_l == pre_r:
                return root

            left_root_val = preorder[pre_l + 1]
            left_root_post = post_pos[left_root_val]

            left_size = left_root_post - post_l + 1

            root.left = build(
                pre_l + 1,
                pre_l + left_size,
                post_l,
                left_root_post,
            )
            root.right = build(
                pre_l + left_size + 1,
                pre_r,
                left_root_post + 1,
                post_r - 1,
            )

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)