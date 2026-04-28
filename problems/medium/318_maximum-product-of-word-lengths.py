from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # Precompute bitmask for each word representing which letters it contains
        # Each bit position (0-25) corresponds to a letter (a-z)
        n = len(words)
        masks = []
        
        for word in words:
            mask = 0
            for char in word:
                # Set the bit corresponding to this character
                mask |= 1 << (ord(char) - ord('a'))
            masks.append(mask)
        
        max_product = 0
        
        # Check all pairs of words
        for i in range(n):
            for j in range(i + 1, n):
                # If bitwise AND is 0, the words share no common letters
                if masks[i] & masks[j] == 0:
                    # Calculate product of lengths
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)
        
        return max_product