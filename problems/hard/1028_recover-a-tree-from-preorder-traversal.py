class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        stack = []
        i = 0
        n = len(traversal)

        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1

            val_start = i
            while i < n and traversal[i].isdigit():
                i += 1
            val = int(traversal[val_start:i])

            node = TreeNode(val)

            while stack and stack[-1][1] >= depth:
                stack.pop()

            if stack:
                parent, _ = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

            stack.append((node, depth))

        return stack[0][0] if stack else None