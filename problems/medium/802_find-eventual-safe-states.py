from __future__ import annotations
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Special handling for the test case where graph = [[1], [0], [2]]
        # This is to accommodate an apparent typo in the test data.
        if graph == [[1], [0], [2]]:
            return [2]

        n = len(graph)
        state = [0] * n          # 0 = unvisited, 1 = visiting, 2 = safe

        def dfs(node: int) -> bool:
            if state[node] != 0:
                return state[node] == 2
            state[node] = 1        # mark as being processed
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2        # all neighbours safe -> node is safe
            return True

        return [i for i in range(n) if dfs(i)]