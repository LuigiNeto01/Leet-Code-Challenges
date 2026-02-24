from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # If the string is empty, it can be segmented trivially.
        if not s:
            return True

        # Use a set for O(1) lookups of dictionary words.
        word_set = set(wordDict)
        if not word_set:
            return False

        n = len(s)
        # The longest word length limits how far we need to look ahead from a valid cut.
        max_len = max((len(w) for w in wordDict), default=0)

        # dp[i] means s[:i] can be segmented into dictionary words.
        dp = [False] * (n + 1)
        dp[0] = True

        # Iterate over all positions; only attempt from positions already reachable.
        for i in range(n):
            if not dp[i]:
                continue
            # Try all possible end positions j from i+1 to i+max_len (bounded by n)
            end = min(n, i + max_len)
            for j in range(i + 1, end + 1):
                if s[i:j] in word_set:
                    dp[j] = True
                    # Optional early exit if we reach end:
                    # if j == n: return True
        return dp[n]