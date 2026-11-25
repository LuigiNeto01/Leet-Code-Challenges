from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Precompute character counts for the available pool of chars.
        chars_count = Counter(chars)
        total = 0
        
        # For each word, check if it can be formed.
        for word in words:
            # Count characters in the current word.
            word_count = Counter(word)
            
            # Verify if chars has enough of each needed character.
            # If any character needed exceeds what's available, skip this word.
            for ch, need in word_count.items():
                if need > chars_count.get(ch, 0):
                    break
            else:
                # If loop didn't break (all needed chars available), word is good.
                total += len(word)
        
        return total