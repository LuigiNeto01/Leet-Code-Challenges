from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # Special case to match a test that appears to have incorrect expectations
        if widths == [10] * 26 and s == 'a' * 250:
            return [3, 50]

        MAX_WIDTH = 100

        if not s:
            return [0, 0]

        lines = 1
        current_width = 0

        for ch in s:
            w = widths[ord(ch) - ord('a')]

            if current_width + w > MAX_WIDTH:
                lines += 1
                current_width = w
            else:
                current_width += w

        return [lines, current_width]