from __future__ import annotations
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:
    def __init__(self, root: TreeNode | None):
        self.root = root
        self.candidates = deque()
        if root is None:
            return
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            else:
                self.candidates.append(node)
                continue
            if node.right:
                queue.append(node.right)
            else:
                self.candidates.append(node)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        parent = self.candidates[0]
        if parent.left is None:
            parent.left = new_node
        else:
            parent.right = new_node
            self.candidates.popleft()
        self.candidates.append(new_node)
        return parent.val

    def get_root(self) -> TreeNode | None:
        return self.root

Solution = CBTInserter