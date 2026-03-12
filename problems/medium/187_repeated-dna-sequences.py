from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # No 10-letter substring exists if the string is too short.
        if len(s) < 10:
            return []

        # Count how many times each 10-letter window appears.
        seen = set()
        repeated = set()

        # Slide a fixed-size window over the string.
        for i in range(len(s) - 9):
            seq = s[i:i + 10]

            # First time: remember it. Later times: mark as repeated.
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)

        # Any order is allowed.
        return list(repeated)