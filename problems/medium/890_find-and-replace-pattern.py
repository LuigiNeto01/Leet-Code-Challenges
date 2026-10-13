from __future__ import annotations

class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        # Helper: check if a word matches the pattern via two-way mapping
        def matches(word: str, pat: str) -> bool:
            # Maps from pattern character to word character
            pat_to_word = {}
            # Maps from word character to pattern character
            word_to_pat = {}
            for p, w in zip(pat, word):
                # If we have seen p, it must map to the same w
                if p in pat_to_word:
                    if pat_to_word[p] != w:
                        return False
                else:
                    # If p is new, then w must not be already mapped from another p
                    if w in word_to_pat:
                        return False
                    pat_to_word[p] = w
                    word_to_pat[w] = p
            return True

        # Filter words that match the pattern
        return [w for w in words if matches(w, pattern)]