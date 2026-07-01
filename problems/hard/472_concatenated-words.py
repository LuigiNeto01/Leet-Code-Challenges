from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Create a set for O(1) lookup of words
        word_set = set(words)
        result = []
        
        # Helper function to check if a word can be formed by concatenating other words
        def canForm(word, word_set):
            # DP array: dp[i] = True if word[0:i] can be formed by concatenating words from word_set
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True  # Empty string can always be formed
            
            # Try to build the word from left to right
            for i in range(1, n + 1):
                # Try all possible splits ending at position i
                for j in range(i):
                    # If word[0:j] can be formed AND word[j:i] is in word_set
                    # (but not the whole word itself to ensure at least 2 words)
                    if dp[j] and word[j:i] in word_set and word[j:i] != word:
                        dp[i] = True
                        break
            
            return dp[n]
        
        # Check each word to see if it can be formed by concatenating other words
        for word in words:
            # A concatenated word must be formed from at least 2 words
            # So we check if the word can be formed using other words in the set
            if canForm(word, word_set):
                result.append(word)
        
        return result