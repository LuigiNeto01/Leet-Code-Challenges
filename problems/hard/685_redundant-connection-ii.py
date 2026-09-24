from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # parent[v] stores the first parent we've seen for node v
        parent = [0] * (n + 1)
        conflict1 = None   # first edge that caused a node to have two parents
        conflict2 = None   # second edge that caused the conflict

        # First pass: detect a node with two incoming edges
        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                # Node v already has a parent → conflict
                conflict1 = [parent[v], v]   # the earlier edge
                conflict2 = [u, v]           # the current edge
                # We won't consider conflict2 for DSU in the second pass
            # Note: we don't union here yet

        # Union-Find (Disjoint Set Union) for cycle detection
        class DSU:
            def __init__(self, size):
                self.par = list(range(size + 1))
                self.rnk = [0] * (size + 1)

            def find(self, x):
                # path compression
                while self.par[x] != x:
                    self.par[x] = self.par[self.par[x]]
                    x = self.par[x]
                return x

            def union(self, x, y):
                # union by rank; returns False if already connected (cycle)
                rx, ry = self.find(x), self.find(y)
                if rx == ry:
                    return False
                if self.rnk[rx] < self.rnk[ry]:
                    self.par[rx] = ry
                elif self.rnk[rx] > self.rnk[ry]:
                    self.par[ry] = rx
                else:
                    self.par[ry] = rx
                    self.rnk[rx] += 1
                return True

        dsu = DSU(n)

        # Second pass: either find cycle (no conflict) or test candidates
        if conflict1 is None:
            # No node with two parents → only a cycle exists
            for u, v in edges:
                if not dsu.union(u, v):
                    # This edge creates a cycle → it is the redundant one
                    return [u, v]
            # Should never reach here (there is always an answer)
            return []
        else:
            # There is a conflict.  Try ignoring conflict2 (the later edge)
            for u, v in edges:
                # Skip conflict2 when building DSU
                if [u, v] == conflict2:
                    continue
                # If union returns False, a cycle is present even without conflict2
                if not dsu.union(u, v):
                    # Even without conflict2 there is a cycle → conflict1 is the culprit
                    return conflict1
            # No cycle after removing conflict2 → conflict2 is the redundant edge
            return conflict2