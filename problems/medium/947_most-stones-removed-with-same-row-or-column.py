from __future__ import annotations
from collections import defaultdict

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        parent = {}
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> None:
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx
        
        for x, y in stones:
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y
            union(x, y)
        
        components = len({find(key) for key in parent})
        return len(stones) - components