from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j] = max subset size using at most i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            # Count resource cost of taking this string once
            zeros = s.count('0')
            ones = len(s) - zeros
            
            # Iterate backward so each string is used at most once
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # Either skip this string or take it and add 1
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        
        # Best answer within full zero/one budget
        return dp[m][n]