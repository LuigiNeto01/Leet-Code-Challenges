from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # -1: uncolored, 0 and 1 are the two colors (sets A and B)
        colors = [-1] * n
        
        for start in range(n):
            if colors[start] != -1:
                continue  # already colored, part of previous componente
            
            # BFS from this uncolored node
            colors[start] = 0  # assign first color
            q = deque([start])
            
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if colors[v] == -1:
                        # assign opposite color
                        colors[v] = 1 - colors[u]
                        q.append(v)
                    elif colors[v] == colors[u]:
                        # conflict: edge connects two nodes of same set
                        return False
        return True