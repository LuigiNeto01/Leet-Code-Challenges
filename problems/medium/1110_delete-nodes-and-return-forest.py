from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # Convert to set for O(1) lookups
        delete_set = set(to_delete)
        forest = []  # collects the roots of the remaining trees

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            """Post-order traversal: returns node if it should be kept, or None if deleted."""
            if not node:
                return None

            # Recursively process children first (so deletions happen bottom-up)
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in delete_set:
                # Node is deleted – its kept children become new roots
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                # Remove this node by returning None
                return None
            else:
                # Node is kept, return it with updated children
                return node

        # Start the recursion from the root
        remaining_root = dfs(root)
        # If the original root survived, it becomes part of the forest
        if remaining_root:
            forest.append(remaining_root)

        return forest