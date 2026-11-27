from __future__ import annotations

class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        # Build adjacency list for undirected graph
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Arrays for DFS timestamps and low-link values
        # tim[u] = discovery time of node u (0 means unvisited)
        tim = [0] * n
        low = [0] * n
        
        # Track visited nodes: use discovery time > 0 as visited indicator
        # We'll assign times starting from 1
        timer = 0
        result = []  # Store critical connections
        
        def dfs(u: int, parent: int) -> None:
            nonlocal timer
            timer += 1
            tim[u] = timer
            low[u] = timer
            
            for v in graph[u]:
                if v == parent:
                    # Skip edge back to parent to avoid false cycle detection
                    continue
                if tim[v] == 0:
                    # v not visited yet; recursively explore
                    dfs(v, u)
                    # After exploring, propagate low-link value from v to u
                    low[u] = min(low[u], low[v])
                    # If the lowest reachable node from v (including v) is deeper 
                    # than u's discovery time, then edge u-v is a bridge
                    if low[v] > tim[u]:
                        result.append([u, v])
                else:
                    # v is already visited (back edge), update low[u] with discovery time of v
                    low[u] = min(low[u], tim[v])
        
        # Graph is guaranteed connected (by problem statement), but we handle multiple components anyway
        for i in range(n):
            if tim[i] == 0:
                dfs(i, -1)
        
        return result