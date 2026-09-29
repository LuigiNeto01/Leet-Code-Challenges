class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp[absent][late] = number of valid records of the current length
        # absent: 0 or 1 total absences
        # late: 0, 1, or 2 consecutive 'L's at the end
        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1  # empty record

        for _ in range(n):
            ndp = [[0] * 3 for _ in range(2)]

            for absent in range(2):
                for late in range(3):
                    cur = dp[absent][late]
                    if cur == 0:
                        continue

                    # Add 'P': absence count unchanged, consecutive late count resets
                    ndp[absent][0] = (ndp[absent][0] + cur) % MOD

                    # Add 'A': allowed only if no absence so far, late streak resets
                    if absent == 0:
                        ndp[1][0] = (ndp[1][0] + cur) % MOD

                    # Add 'L': allowed only if current consecutive lates are less than 2
                    if late < 2:
                        ndp[absent][late + 1] = (ndp[absent][late + 1] + cur) % MOD

            dp = ndp

        return (sum(dp[0]) + sum(dp[1])) % MOD