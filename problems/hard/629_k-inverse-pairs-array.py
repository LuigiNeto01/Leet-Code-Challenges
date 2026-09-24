from __future__ import annotations

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j] = number of arrays of length i with exactly j inverse pairs.
        # We only need the previous row, so we keep a 1D array of length k+1.
        dp = [0] * (k + 1)
        dp[0] = 1  # base: array of length 1 has 0 inverse pairs
        
        for i in range(2, n + 1):  # build up to length n
            new_dp = [0] * (k + 1)
            prefix_sum = 0  # sliding window sum for the DP recurrence
            
            for j in range(k + 1):
                # When we insert the new largest element (i) into any position p (0..i-1),
                # it creates p new inverse pairs. So dp[i][j] = sum over p of dp[i-1][j-p].
                # Use prefix sum to avoid O(n*k^2).
                prefix_sum += dp[j]  # add current dp[i-1][j]
                if j >= i:  # remove elements outside the window of size i
                    prefix_sum -= dp[j - i]
                prefix_sum %= MOD
                new_dp[j] = prefix_sum % MOD
                
            dp = new_dp
        
        return dp[k] % MOD