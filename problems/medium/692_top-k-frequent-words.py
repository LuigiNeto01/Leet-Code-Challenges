from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count frequencies of each word
        freq = Counter(words)
        
        # Sort unique words by:
        # 1) frequency descending (most frequent first)
        # 2) lexicographical ascending for ties
        sorted_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))
        
        # Return the first k words
        return sorted_words[:k]