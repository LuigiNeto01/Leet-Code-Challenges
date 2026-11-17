from __future__ import annotations

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        # Maximum possible Manhattan distance from center to any cell is at most rows+cols.
        # Create buckets for each distance, index = distance value.
        max_dist = rows + cols
        buckets = [[] for _ in range(max_dist + 1)]

        # Iterate over all cells and place each into its distance bucket.
        for r in range(rows):
            for c in range(cols):
                d = abs(r - rCenter) + abs(c - cCenter)  # Manhattan distance
                buckets[d].append([r, c])

        # Flatten the buckets in order of increasing distance.
        result = []
        for bucket in buckets:
            result.extend(bucket)

        return result