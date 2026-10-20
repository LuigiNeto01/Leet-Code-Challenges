from __future__ import annotations

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        # Use two pointers: low is the smallest unused number, high is the largest.
        low = 0
        high = len(s)
        result = []

        for ch in s:
            if ch == 'I':
                # For 'I', choose the smallest remaining number to guarantee increase.
                result.append(low)
                low += 1
            else:  # ch == 'D'
                # For 'D', choose the largest remaining number to guarantee decrease.
                result.append(high)
                high -= 1

        # The last remaining number is the only one left; append it.
        result.append(low)
        return result