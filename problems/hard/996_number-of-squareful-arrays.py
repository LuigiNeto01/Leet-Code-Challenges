from typing import List
from collections import Counter
from functools import lru_cache
from math import isqrt

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        if len(nums) == 2:
            s = nums[0] + nums[1]
            r = isqrt(s)
            return 1 if r * r == s else 0

        freq = Counter(nums)
        vals = list(freq.keys())
        m = len(vals)

        can = [[False] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                s = vals[i] + vals[j]
                r = isqrt(s)
                can[i][j] = (r * r == s)

        @lru_cache(None)
        def dfs(counts, last):
            if not any(counts):
                return 1

            ans = 0
            for nxt in range(m):
                if counts[nxt] == 0:
                    continue
                if last == -1 or can[last][nxt]:
                    new_counts = list(counts)
                    new_counts[nxt] -= 1
                    ans += dfs(tuple(new_counts), nxt)

            return ans

        start_counts = tuple(freq[v] for v in vals)
        return dfs(start_counts, -1)