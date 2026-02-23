class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Quick length check: interleaving preserves total length
        if len(s1) + len(s2) != len(s3):
            return False

        n, m = len(s1), len(s2)

        # dp[j] will be True if s3[:i+j] is an interleaving of
        # s1[:i] and s2[:j] for the current i (outer loop) and j (inner loop).
        dp = [False] * (m + 1)

        # Base case: i = 0, only s2 contributes
        dp[0] = True
        for j in range(1, m + 1):
            # Can we form s3[:j] using only s2[:j]?
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Iterate over s1 characters
        for i in range(1, n + 1):
            # First column: j = 0, only s1 contributes up to i
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, m + 1):
                # Option 1: take current char from s1
                # dp[j] here still represents dp[i-1][j] before update
                take_from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]

                # Option 2: take current char from s2
                # dp[j-1] now represents dp[i][j-1] after previous update in this row
                take_from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]

                dp[j] = take_from_s1 or take_from_s2

        # Result for full strings: interleaving possible iff dp[m] is True
        return dp[m]