from __future__ import annotations
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # Convert banned list to a set for O(1) lookup
        banned_set = set(banned)
        
        # Split paragraph into words: all non-letter characters act as delimiters
        # re.findall with pattern r'\w+' extracts sequences of word characters
        # Convert each word to lowercase for case-insensitive comparison
        words = re.findall(r'\w+', paragraph.lower())
        
        # Count frequencies of words that are not banned
        # Using a generator to avoid storing intermediate list of filtered words
        word_counts = Counter(word for word in words if word not in banned_set)
        
        # most_common(1) returns list of (word, count) tuples; extract the word
        return word_counts.most_common(1)[0][0]