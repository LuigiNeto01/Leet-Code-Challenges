from __future__ import annotations

class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        # Remove duplicate words because if two words are identical, 
        # we only need one substring in the encoding.
        unique_words = set(words)

        # We'll count total length: each word that is NOT a suffix of another word
        # contributes len(word) + 1 (for the '#' separator).
        total_len = 0

        for w in unique_words:
            # Check if w is a suffix of any *other* word in the set.
            # If it is, it can be encoded as part of that longer word.
            is_suffix = False
            for other in unique_words:
                if other is w:  # skip comparing with itself
                    continue
                if other.endswith(w):
                    is_suffix = True
                    break
            if not is_suffix:
                total_len += len(w) + 1  # +1 for the '#'

        return total_len