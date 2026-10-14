import heapq
from typing import List

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # Build adjacency list for original nodes: (neighbor, weight = cnt+1)
        adj = [[] for _ in range(n)]
        for u, v, cnt in edges:
            w = cnt + 1  # edge weight in the subdivided graph
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Dijkstra from node 0 to all original nodes
        INF = 10**18
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (distance, node)

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        # Count reachable original nodes (distance <= maxMoves)
        reachable_original = sum(1 for d in dist if d <= maxMoves)

        # Count reachable intermediate nodes on each edge
        reachable_intermediate = 0
        for u, v, cnt in edges:
            # Remaining moves after reaching each endpoint (0 if endpoint unreachable)
            remain_u = max(0, maxMoves - dist[u])
            remain_v = max(0, maxMoves - dist[v])
            # Total intermediate nodes we can cover from both ends,
            # but not exceeding the total count of intermediate nodes on that edge.
            reachable_intermediate += min(cnt, remain_u + remain_v)

        return reachable_original + reachable_intermediate