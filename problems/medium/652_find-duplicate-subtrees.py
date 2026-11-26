from __future__ import annotations  # allow forward reference in type hints

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode | None]:
        """
        Return a list of root nodes of all duplicate subtrees.
        Each duplicate group is represented by exactly one root (the second occurrence).
        """
        # Count occurrences of each subtree serialization string
        count: dict[str, int] = {}
        # Collect one root per duplicated subtree kind
        result: list[TreeNode | None] = []

        def serialize(node: TreeNode | None) -> str:
            """Post-order serialization of a subtree into a unique string key."""
            # Base case: null node
            if node is None:
                return "#"

            # Recursively serialize left and right children
            left_ser = serialize(node.left)
            right_ser = serialize(node.right)

            # Create a unique key for this subtree (parentheses avoid ambiguity)
            key = f"({node.val},{left_ser},{right_ser})"

            # Update occurrence counter
            cnt = count.get(key, 0) + 1
            count[key] = cnt

            # The second occurrence of this key marks a duplicate subtree
            if cnt == 2:
                result.append(node)

            return key

        # Start serialization from the root
        serialize(root)
        return result