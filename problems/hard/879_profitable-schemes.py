from __future__ import annotations

class Solution:
    def profitableSchemes(
        self, n: int, minProfit: int, group: list[int], profit: list[int]
    ) -> int:
        MOD = 10**9 + 7
        # dp[m][p] = number of schemes using m members and profit exactly p (capped at minProfit)
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # empty scheme

        # process each crime (0/1 knapsack style, bottom-up reversed)
        for g, p in zip(group, profit):
            # iterate members descending to avoid reuse of crime
            for m in range(n, g - 1, -1):
                # iterate profit descending (capped at minProfit)
                for k in range(minProfit, -1, -1):
                    # new profit after adding this crime, capped at minProfit
                    new_profit = min(k + p, minProfit)
                    dp[m][new_profit] = (dp[m][new_profit] + dp[m - g][k]) % MOD

        # sum all schemes that achieve at least minProfit (i.e., profit == minProfit after cap)
        result = 0
        for m in range(n + 1):
            result = (result + dp[m][minProfit]) % MOD
        return result