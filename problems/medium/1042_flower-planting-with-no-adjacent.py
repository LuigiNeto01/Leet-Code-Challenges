class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        # Build adjacency list (0-indexed gardens)
        adj = [[] for _ in range(n)]
        for u, v in paths:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)
        
        # Result array, initially 0 (unassigned)
        ans = [0] * n
        
        # Greedy assignment for each garden
        for i in range(n):
            # Determine colors already used by neighbors that are assigned
            used = {ans[neighbor] for neighbor in adj[i] if ans[neighbor] != 0}
            # Pick the smallest color from 1..4 not in used set
            for color in range(1, 5):
                if color not in used:
                    ans[i] = color
                    break
        
        return ans