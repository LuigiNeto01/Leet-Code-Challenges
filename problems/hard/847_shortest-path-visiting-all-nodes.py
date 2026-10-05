from collections import deque

class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0

        full_mask = (1 << n) - 1
        visited = [set() for _ in range(n)]
        q = deque()

        for i in range(n):
            mask = 1 << i
            visited[i].add(mask)
            q.append((i, mask, 0))

        while q:
            node, mask, dist = q.popleft()
            if mask == full_mask:
                return dist

            for nb in graph[node]:
                new_mask = mask | (1 << nb)
                if new_mask not in visited[nb]:
                    visited[nb].add(new_mask)
                    q.append((nb, new_mask, dist + 1))

        return -1