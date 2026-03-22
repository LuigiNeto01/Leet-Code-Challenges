from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp[i] stores the number of set bits in i
        dp = [0] * (n + 1)

        # For any i:
        # - i >> 1 removes the last bit
        # - i & 1 tells whether the last bit is 1
        # So bits(i) = bits(i >> 1) + (i & 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp