from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sorting lets us stop early once numbers become too large.
        candidates.sort()
        result: List[List[int]] = []
        path: List[int] = []

        def dfs(start: int, remaining: int) -> None:
            # Found an exact sum, so record the current combination.
            if remaining == 0:
                result.append(path[:])
                return

            # Try each candidate from 'start' onward to avoid duplicate orders.
            for i in range(start, len(candidates)):
                value = candidates[i]

                # Because candidates are sorted, later values will also be too large.
                if value > remaining:
                    break

                # Choose this value and stay at i since reuse is allowed.
                path.append(value)
                dfs(i, remaining - value)
                # Backtrack to explore the next choice.
                path.pop()

        dfs(0, target)
        return result