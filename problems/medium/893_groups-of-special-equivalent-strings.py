class Solution:
    def numSpecialEquivGroups(self, words: list[str]) -> int:
        # Use a set to store the canonical signature of each word.
        # Two words are special-equivalent if they have the same sorted
        # characters at even indices and same sorted characters at odd indices.
        
        seen = set()
        
        for w in words:
            # Extract characters at even indices (0,2,4,...) and odd indices (1,3,5,...)
            even_chars = sorted(w[0::2])  # list of chars at even positions
            odd_chars = sorted(w[1::2])   # list of chars at odd positions
            
            # Build a signature tuple: (evens_tuple, odds_tuple)
            # Using tuple because it's hashable (can be stored in a set)
            signature = (tuple(even_chars), tuple(odd_chars))
            seen.add(signature)
        
        # The number of distinct groups equals the number of unique signatures
        return len(seen)