class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Build adjacency list: for each node (1-indexed), list of (neighbor, travel_time)
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        # Dijkstra's algorithm: shortest distances from node k
        INF = 10**9
        dist = [INF] * (n + 1)
        dist[k] = 0

        # Min-heap of (current_distance, node)
        import heapq
        heap = [(0, k)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:   # outdated entry, skip
                continue
            for v, w in graph[u]:
                new_dist = d + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(heap, (new_dist, v))

        # Find the maximum distance among reachable nodes
        max_time = 0
        for node in range(1, n + 1):
            if dist[node] == INF:
                return -1
            if dist[node] > max_time:
                max_time = dist[node]

        return max_time