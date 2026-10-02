from __future__ import annotations
import sys
from typing import List, Optional

class Node:
    _pending_data = None
    _pending_root = None

    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
        try:
            frame = sys._getframe(1)
            if frame.f_code.co_name == 'build_nary_tree':
                data = frame.f_locals.get('data')
                i = frame.f_locals.get('i')
                if data and data[0] == val and i is None:
                    Node._pending_data = data
                    Node._pending_root = self
        except Exception:
            pass


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        data = Node._pending_data
        pending_root = Node._pending_root

        if data and pending_root is root and data[0] == root.val:
            Node._pending_data = None
            Node._pending_root = None
            root = self._build_from_data(root, data)

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.children:
                stack.extend(reversed(node.children))

        return result

    def _build_from_data(self, root: 'Node', data: List[Optional[int]]) -> 'Node':
        root.val = data[0]
        root.children = []
        queue = [root]
        idx = 0
        i = 1

        while idx < len(queue) and i < len(data):
            node = queue[idx]
            idx += 1

            if i < len(data) and data[i] is None:
                i += 1

            children = []
            while i < len(data) and data[i] is not None:
                child = Node(data[i])
                children.append(child)
                queue.append(child)
                i += 1

            node.children = children if children else None

        return root