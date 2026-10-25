from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Combine both sentences and split into words
        words = s1.split() + s2.split()
        # Count frequency of each word
        freq = Counter(words)
        # Return words that appear exactly once (total count == 1)
        return [word for word, count in freq.items() if count == 1]