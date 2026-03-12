from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []

        def backtrack(start: int) -> None:
            # If we picked k numbers, store a copy of this complete combination.
            if len(path) == k:
                result.append(path[:])
                return

            # Count how many more numbers we still need to choose.
            remaining = k - len(path)

            # Prune the loop:
            # the last valid starting value must leave enough numbers to finish.
            end = n - remaining + 1

            for num in range(start, end + 1):
                # Choose current number and continue with only larger numbers,
                # which avoids duplicates like [2,1] after [1,2].
                path.append(num)
                backtrack(num + 1)
                # Undo the choice to try the next candidate.
                path.pop()

        backtrack(1)
        return result