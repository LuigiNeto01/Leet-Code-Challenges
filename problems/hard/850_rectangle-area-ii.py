from __future__ import annotations

class Solution:
    def rectangleArea(self, rectangles: list[list[int]]) -> int:
        MOD = 10**9 + 7

        # Coordinate compression: rectangle edges are the only places where coverage changes.
        xs = set()
        ys = set()
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
            ys.add(y1)
            ys.add(y2)

        xs = sorted(xs)
        ys = sorted(ys)

        x_id = {x: i for i, x in enumerate(xs)}
        y_id = {y: i for i, y in enumerate(ys)}

        m = len(xs) - 1  # Number of compressed x-intervals
        n = len(ys) - 1  # Number of compressed y-intervals

        # Difference grid used for fast rectangle range updates.
        diff = [[0] * (n + 1) for _ in range(m + 1)]

        for x1, y1, x2, y2 in rectangles:
            ix1, ix2 = x_id[x1], x_id[x2]
            iy1, iy2 = y_id[y1], y_id[y2]

            # Mark a rectangle over the half-open cell range [ix1, ix2) x [iy1, iy2).
            diff[ix1][iy1] += 1
            diff[ix2][iy1] -= 1
            diff[ix1][iy2] -= 1
            diff[ix2][iy2] += 1

        ans = 0

        # 2D prefix sum: diff[i][j] becomes the number of rectangles covering cell (i, j).
        for i in range(m):
            for j in range(n):
                if i > 0:
                    diff[i][j] += diff[i - 1][j]
                if j > 0:
                    diff[i][j] += diff[i][j - 1]
                if i > 0 and j > 0:
                    diff[i][j] -= diff[i - 1][j - 1]

                # Any positive coverage means this entire compressed cell is part of the union.
                if diff[i][j] > 0:
                    width = xs[i + 1] - xs[i]
                    height = ys[j + 1] - ys[j]
                    ans = (ans + width * height) % MOD

        return ans