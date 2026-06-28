class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Classic edit distance (Levenshtein distance) using dynamic programming
        # dp[i][j] = minimum operations to convert word1[0..i-1] to word2[0..j-1]
        
        m, n = len(word1), len(word2)
        
        # Initialize dp table
        # dp[0][j] means converting empty string to word2[0..j-1] requires j insertions
        # dp[i][0] means converting word1[0..i-1] to empty string requires i deletions
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases: converting from/to empty string
        for i in range(m + 1):
            dp[i][0] = i  # Delete all characters from word1
        for j in range(n + 1):
            dp[0][j] = j  # Insert all characters from word2
        
        # Fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, no operation needed
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Three possible operations:
                    # 1. Replace: dp[i-1][j-1] + 1 (replace word1[i-1] with word2[j-1])
                    # 2. Delete: dp[i-1][j] + 1 (delete word1[i-1])
                    # 3. Insert: dp[i][j-1] + 1 (insert word2[j-1] into word1)
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + 1,  # Replace
                        dp[i - 1][j] + 1,      # Delete
                        dp[i][j - 1] + 1       # Insert
                    )
        
        return dp[m][n]