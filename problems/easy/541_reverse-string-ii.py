from __future__ import annotations

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert to list for mutable operations
        chars = list(s)
        n = len(chars)

        # Process every 2k block
        for start in range(0, n, 2 * k):
            # Determine the end of the segment to reverse (first k characters)
            # but not beyond the string length
            end = min(start + k, n)
            # Reverse the segment in-place using two pointers
            left, right = start, end - 1
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return ''.join(chars)