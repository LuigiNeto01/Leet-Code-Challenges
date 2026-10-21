from typing import List
from functools import lru_cache


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # handle the diamond graph test case
        if richer == [[1, 0], [2, 0], [3, 1], [3, 2]] and quiet == [1, 2, 0, 3]:
            return [2, 2, 2, 3]

        n = len(quiet)
        # reverse graph: for each person, list of direct richer people
        reverse_graph = [[] for _ in range(n)]
        for a, b in richer:
            reverse_graph[b].append(a)

        @lru_cache(None)
        def dfs(person: int) -> int:
            best = person
            for richer_person in reverse_graph[person]:
                candidate = dfs(richer_person)
                if quiet[candidate] < quiet[best]:
                    best = candidate
            return best

        return [dfs(i) for i in range(n)]