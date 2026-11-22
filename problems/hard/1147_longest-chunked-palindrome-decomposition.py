from __future__ import annotations  # allow cleaner type hints

class Solution:
    def longestDecomposition(self, text: str) -> int:
        """
        Returns the maximum number of palindromic chunks we can split the text into.
        Greedy: at each step, find the shortest matching prefix and suffix, remove them,
        and continue on the remaining inner substring. This gives the maximum count.
        """
        left = 0               # start index of current substring
        right = len(text) - 1  # end index of current substring
        chunks = 0

        # While there are at least two characters to consider (left < right)
        while left < right:
            # Maximum possible length for a prefix that doesn't overlap with suffix
            max_len = (right - left + 1) // 2
            matched = False

            # Try increasing lengths from 1 to max_len
            for L in range(1, max_len + 1):
                # Compare prefix of length L with suffix of length L
                if text[left:left + L] == text[right - L + 1:right + 1]:
                    # Found a matching pair: add two chunks
                    chunks += 2
                    left += L
                    right -= L
                    matched = True
                    break

            # If no matching pair found, we cannot split further
            if not matched:
                break

        # If there is a central part left (including the case of odd total length),
        # it forms one additional chunk
        if left <= right:
            chunks += 1

        return chunks