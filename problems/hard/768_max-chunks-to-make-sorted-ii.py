from __future__ import annotations

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        n = len(arr)

        # prefix_max[i] = maximum value in arr[0..i]
        prefix_max = [0] * n
        prefix_max[0] = arr[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        # suffix_min[i] = minimum value in arr[i..n-1]
        suffix_min = [0] * n
        suffix_min[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])

        # A cut after i is valid if every element on the left is <= every element on the right.
        # All valid cuts can be taken together to maximize the number of chunks.
        chunks = 1
        for i in range(n - 1):
            if prefix_max[i] <= suffix_min[i + 1]:
                chunks += 1

        return chunks