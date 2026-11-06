from __future__ import annotations
from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        # Start with character counts of the first word
        common = Counter(words[0])

        # Intersect the counts with each subsequent word
        for word in words[1:]:
            current = Counter(word)
            # Counter intersection keeps only keys present in both,
            # and takes the minimum count for each key.
            common &= current

        # Expand the final counts into a list of characters
        result = []
        for ch, cnt in common.items():
            result.extend([ch] * cnt)
        return result