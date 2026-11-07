class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        # dp[i][j] = number of playlists of length i that use exactly j different songs
        # dp[0][0] = 1 (empty playlist uses 0 songs)
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            # at length i, we can have at most min(i, n) distinct songs
            for j in range(1, min(i, n) + 1):
                # Option 1: add a new song that hasn't been played before.
                # There are (n - (j-1)) such songs to choose from.
                dp[i][j] = dp[i-1][j-1] * (n - (j - 1)) % MOD

                # Option 2: repeat an already played song.
                # We can only repeat a song if at least k other songs have been played since its last occurrence.
                # Number of eligible songs to repeat is j - k (if j > k).
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i-1][j] * (j - k)) % MOD

        # The answer is the number of playlists of length goal that use all n songs.
        return dp[goal][n] % MOD