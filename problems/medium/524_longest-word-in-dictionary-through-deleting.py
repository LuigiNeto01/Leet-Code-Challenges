class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        # Helper to check if word is a subsequence of s (by deleting characters)
        def is_subsequence(word: str) -> bool:
            i = 0  # pointer in s
            # For each character in word, find its match in s in order
            for ch in word:
                # Advance i until we find ch or reach end
                while i < len(s) and s[i] != ch:
                    i += 1
                if i == len(s):  # reached end without finding ch
                    return False
                i += 1  # move past the matched character
            return True
        
        best = ""  # current best result
        for word in dictionary:
            # Only consider if word can be formed and is longer, or same length but lexicographically smaller
            if (is_subsequence(word) and 
                (len(word) > len(best) or (len(word) == len(best) and word < best))):
                best = word
        return best