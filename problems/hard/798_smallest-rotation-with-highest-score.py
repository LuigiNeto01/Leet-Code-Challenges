from __future__ import annotations

class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        n = len(nums)
        diff = [0] * (n + 1)

        for i, v in enumerate(nums):
            # After rotation by k, original index i goes to (i - k) % n.
            # It scores when (i - k) % n >= v.
            # The valid k values form a cyclic interval:
            # start = (i + 1) % n, end = (i - v) % n.
            start = (i + 1) % n
            end = (i - v) % n

            if start <= end:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                # Wrapped interval: [start, n-1] and [0, end]
                diff[start] += 1
                diff[0] += 1
                diff[end + 1] -= 1

        # Prefix sum over diff gives the score for each rotation k.
        best_k = 0
        best_score = -1
        cur = 0
        for k in range(n):
            cur += diff[k]
            # Strict > keeps the smallest k in case of ties.
            if cur > best_score:
                best_score = cur
                best_k = k

        return best_k