class Solution:
    def longestWord(self, words: list[str]) -> str:
        # Sort words lexicographically; then if two words target same length,
        # the smaller one will be processed first, aligning with tie-breaking.
        words.sort()
        
        # Keep a set of all valid prefixes built from shorter words.
        # An empty string is trivially a valid prefix.
        valid_prefixes = set()
        valid_prefixes.add("")
        
        # Track the best word found so far (longest, then lexicographically smallest).
        best = ""
        
        for word in words:
            # A word can be built if its prefix (without last char) is already valid.
            # Since words are processed sorted, all shorter prefixes should be checked.
            if word[:-1] in valid_prefixes:
                # Mark this word as a valid prefix for longer words.
                valid_prefixes.add(word)
                # Update best if this word is longer, or same length but lexicographically smaller.
                # Because we process sorted, equal-length words already come in lexicographic order,
                # so we only need to check length.
                if len(word) > len(best):
                    best = word
                # If lengths equal, we keep the first one encountered (which is smaller due to sort).
        
        return best