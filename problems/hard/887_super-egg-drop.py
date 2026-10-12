class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[e] = maximum floors we can handle with the current move count and e eggs.
        dp = [0] * (k + 1)
        moves = 0

        # Keep adding moves until the current eggs can cover all n floors.
        while dp[k] < n:
            moves += 1

            # Update from high eggs to low so dp[eggs - 1] still uses
            # the value from the previous move count.
            for eggs in range(k, 0, -1):
                # Break case: dp[eggs - 1] floors below.
                # Survive case: old dp[eggs] floors above.
                # The chosen drop floor itself adds 1.
                dp[eggs] += dp[eggs - 1] + 1

        return moves