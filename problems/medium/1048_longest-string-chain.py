from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort words by length ascending to process from shortest to longest
        words.sort(key=len)
        # dp[word] = longest chain length ending at word
        dp = {}
        max_chain = 1  # single word is always a chain of length 1

        for word in words:
            best = 0
            # Try removing each character to get a possible predecessor
            for i in range(len(word)):
                # Remove character at index i
                pred = word[:i] + word[i+1:]
                # If predecessor exists, remember its chain length
                if pred in dp:
                    best = max(best, dp[pred])
            # Current word extends the best predecessor chain by 1
            dp[word] = best + 1
            # Keep the global maximum
            max_chain = max(max_chain, dp[word])

        return max_chain