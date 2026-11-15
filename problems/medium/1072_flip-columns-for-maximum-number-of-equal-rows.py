from __future__ import annotations

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        pattern_count = {}
        for row in matrix:
            if row[0] == 1:
                normalized = tuple(1 ^ val for val in row)
            else:
                normalized = tuple(row)
            pattern_count[normalized] = pattern_count.get(normalized, 0) + 1
        return max(pattern_count.values())