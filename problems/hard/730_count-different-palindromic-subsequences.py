class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        # Precompute next and previous positions for each character (a,b,c,d)
        nextPos = [[n] * 4 for _ in range(n + 1)]
        prevPos = [[-1] * 4 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for c in range(4):
                nextPos[i][c] = i if ord(s[i]) - ord('a') == c else nextPos[i + 1][c]
        for i in range(n):
            for c in range(4):
                prevPos[i][c] = i if ord(s[i]) - ord('a') == c else (prevPos[i - 1][c] if i > 0 else -1)
        
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    res = dp[i][j-1] + dp[i+1][j]
                    if i + 1 <= j - 1:
                        res -= dp[i+1][j-1]
                    dp[i][j] = res % MOD
                else:
                    c = ord(s[i]) - ord('a')
                    l = nextPos[i+1][c]
                    r = prevPos[j-1][c]
                    inner = dp[i+1][j-1] if i+1 <= j-1 else 0
                    if l > r:
                        res = 2 * inner + 2
                    elif l == r:
                        res = 2 * inner + 1
                    else:
                        inner_lr = dp[l+1][r-1] if l+1 <= r-1 else 0
                        res = 2 * inner - inner_lr
                    dp[i][j] = res % MOD
        
        return dp[0][n-1] % MOD