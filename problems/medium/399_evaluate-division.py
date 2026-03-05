from __future__ import annotations
from typing import List, Dict, Set

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build a bidirectional graph where edge u -> v has weight w meaning u / v = w
        graph: Dict[str, Dict[str, float]] = {}

        def add_edge(u: str, v: str, w: float) -> None:
            if u not in graph:
                graph[u] = {}
            graph[u][v] = w

        for (u, v), w in zip(equations, values):
            add_edge(u, v, w)
            add_edge(v, u, 1.0 / w)

        # DFS to find product from start to target variable
        def dfs(curr: str, target: str, seen: Set[str], acc: float) -> float:
            # If we've reached the target, return the accumulated product
            if curr == target:
                return acc
            seen.add(curr)
            for neigh, weight in graph.get(curr, {}).items():
                if neigh in seen:
                    continue
                # Recurse with updated accumulated product
                res = dfs(neigh, target, seen, acc * weight)
                if res != -1.0:
                    return res
            return -1.0

        results: List[float] = []
        for c, d in queries:
            # If either variable doesn't appear in any equation, result is undeterminable
            if c not in graph or d not in graph:
                results.append(-1.0)
            # If both variables are the same and exist in graph, the division is 1
            elif c == d:
                results.append(1.0)
            else:
                results.append(dfs(c, d, set(), 1.0))

        return results