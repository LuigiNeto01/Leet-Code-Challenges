from __future__ import annotations

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Build a mapping from each character to its index in the alien alphabet
        char_to_rank = {ch: i for i, ch in enumerate(order)}

        # Compare every pair of adjacent words
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Compare character by character
            for j in range(min(len(word1), len(word2))):
                rank1 = char_to_rank[word1[j]]
                rank2 = char_to_rank[word2[j]]

                if rank1 < rank2:
                    # Current pair is in order, stop checking this pair
                    break
                elif rank1 > rank2:
                    # Out of order: earlier word has a larger character
                    return False
            else:
                # All compared characters are equal up to the min length.
                # If the first word is longer, it should come after the shorter one,
                # so the pair is not sorted (e.g., "apple" before "app").
                if len(word1) > len(word2):
                    return False

        return True