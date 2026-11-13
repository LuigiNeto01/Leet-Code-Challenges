class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        # We want to keep the longest subsequence of columns such that each row 
        # is non-decreasing. This is a classic Longest Increasing Subsequence (LIS)
        # problem but across columns over multiple strings.
        
        n = len(strs)          # number of strings
        m = len(strs[0])       # length of each string (number of columns)
        
        # dp[i] = length of the longest valid subsequence ending at column i
        dp = [1] * m
        
        for i in range(m):
            for j in range(i):
                # Check if we can append column i after column j without breaking
                # the lexicographic order in any row.
                valid = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        valid = False
                        break
                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The maximum number of columns we can keep
        keep = max(dp) if dp else 0
        # Minimum deletions = total columns - max kept
        return m - keep