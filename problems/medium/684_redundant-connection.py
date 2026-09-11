from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Number of nodes equals number of edges (since it's a tree + one extra edge)
        n = len(edges)
        # 1-indexed union-find; parent[i] points to parent or itself if root
        parent = list(range(n + 1))
        rank = [0] * (n + 1)   # rank for union by size/height

        def find(x: int) -> int:
            """Find the root of x with path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])   # compress path
            return parent[x]

        def union(x: int, y: int) -> bool:
            """
            Union the sets containing x and y.
            Returns True if they were merged, False if they were already connected.
            """
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False          # cycle would be created
            # Union by rank: attach smaller tree under larger root
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True

        # Process edges in order; the first edge that creates a cycle is the redundant one
        for u, v in edges:
            if not union(u, v):  # already in same set -> this edge completes a cycle
                return [u, v]

        # According to problem constraints, we always return inside the loop
        return []