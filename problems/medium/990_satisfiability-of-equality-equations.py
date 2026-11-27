from __future__ import annotations
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Union-Find (Disjoint Set Union) structure to track equality relationships.
        parent = list(range(26))  # 26 lowercase letters: 'a'..'z'
        rank = [0] * 26

        def find(x: int) -> int:
            # Path compression: make every node point directly to the root.
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None:
            # Union by rank: attach the smaller tree under the larger tree.
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        # First pass: process all "==" equations to unite variables.
        for eq in equations:
            if eq[1] == '=':  # "==" equation
                var1 = ord(eq[0]) - ord('a')
                var2 = ord(eq[3]) - ord('a')
                union(var1, var2)

        # Second pass: check all "!=" equations for contradictions.
        for eq in equations:
            if eq[1] == '!':  # "!=" equation
                var1 = ord(eq[0]) - ord('a')
                var2 = ord(eq[3]) - ord('a')
                # If they are already in the same set, the inequality cannot hold.
                if find(var1) == find(var2):
                    return False

        # No contradictions found.
        return True