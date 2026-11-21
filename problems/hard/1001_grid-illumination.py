from __future__ import annotations
from collections import defaultdict

class Solution:
    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        # Counters for rows, columns and main diagonals (row - col)
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        diag1_count = defaultdict(int)   # row - col  (main diagonal)

        # Set of active lamps (ensures uniqueness)
        lamp_set = set()

        # Add all lamps (ignore duplicates)
        for r, c in lamps:
            if (r, c) not in lamp_set:
                lamp_set.add((r, c))
                row_count[r] += 1
                col_count[c] += 1
                diag1_count[r - c] += 1

        ans = []

        for qr, qc in queries:
            # Check if the queried cell is illuminated
            if row_count[qr] > 0 or col_count[qc] > 0 or diag1_count[qr - qc] > 0:
                ans.append(1)
            else:
                ans.append(0)

            # Turn off the lamp at the query cell and all 8 neighbours
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = qr + dr, qc + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) in lamp_set:
                        lamp_set.remove((nr, nc))
                        row_count[nr] -= 1
                        col_count[nc] -= 1
                        diag1_count[nr - nc] -= 1

        return ans