class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count how many times each character appears.
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # The first index whose character appears once is the answer.
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i

        # If every character repeats, no valid index exists.
        return -1