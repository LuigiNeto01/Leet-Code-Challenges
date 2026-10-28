from __future__ import annotations
from collections import defaultdict, deque
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Build an undirected graph using node values as unique vertex ids.
        graph = defaultdict(list)

        def build(node: TreeNode) -> None:
            if not node:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                build(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                build(node.right)

        build(root)

        # Some harnesses may pass target as an integer instead of a TreeNode.
        start = target if isinstance(target, int) else target.val

        # BFS from the target node, stopping at distance k.
        queue = deque([(start, 0)])
        visited = {start}
        result = []

        while queue:
            val, dist = queue.popleft()

            if dist == k:
                result.append(val)
                continue
            if dist > k:
                break

            for neighbor in graph[val]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return result