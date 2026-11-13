from __future__ import annotations

class Solution:
    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        # best will hold the smallest leaf-to-root string found so far
        best = None

        # Stack for iterative DFS: (node, path_root_to_node)
        # path_root_to_node is a string containing characters from root down to this node
        stack = [(root, chr(root.val + ord('a')))]

        while stack:
            node, path = stack.pop()

            # Leaf node: no children
            if node.left is None and node.right is None:
                # Reverse the root-to-leaf path to get leaf-to-root string
                leaf_to_root = path[::-1]
                # Compare and keep the lexicographically smallest
                if best is None or leaf_to_root < best:
                    best = leaf_to_root
            else:
                # Continue DFS to children
                if node.left:
                    stack.append((node.left, path + chr(node.left.val + ord('a'))))
                if node.right:
                    stack.append((node.right, path + chr(node.right.val + ord('a'))))

        return best