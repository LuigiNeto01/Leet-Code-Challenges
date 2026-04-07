class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Different lengths can never be rearrangements of each other.
        if len(s) != len(t):
            return False

        # Count how many times each character appears in s.
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        # Remove characters using t.
        for ch in t:
            # Missing character means t uses something s does not have.
            if ch not in counts:
                return False

            counts[ch] -= 1

            # Clean up zero counts to keep the map meaningful.
            if counts[ch] == 0:
                del counts[ch]
            # Negative count means t uses a character too many times.
            elif counts[ch] < 0:
                return False

        # Empty map means every character matched exactly.
        return not counts