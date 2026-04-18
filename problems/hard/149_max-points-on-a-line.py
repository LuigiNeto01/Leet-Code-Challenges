from typing import List
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # If there are 0,1,2 points, answer is trivial
        n = len(points)
        if n <= 2:
            return n

        max_on_line = 1  # at least one point exists

        # Iterate over each point as the anchor point
        for i in range(n):
            # Use a map from normalized slope (dy,dx) to count of points with that slope w.r.t anchor
            slopes = {}
            duplicates = 0  # count of points exactly equal to anchor (rare if unique constraint holds)
            xi, yi = points[i]
            local_max = 0  # max number of points (excluding anchor duplicates) collinear with anchor

            # Compare anchor with every other point after it to avoid double counting
            for j in range(i + 1, n):
                xj, yj = points[j]
                dx = xj - xi
                dy = yj - yi

                # If the point coincides with the anchor, count duplicate
                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                # Normalize the slope as a reduced fraction (dy, dx)
                # Compute greatest common divisor for reduction
                g = gcd(dy, dx)
                if g != 0:
                    dy_norm = dy // g
                    dx_norm = dx // g
                else:
                    # Should not get here except when both zero handled above
                    dy_norm = dy
                    dx_norm = dx

                # Enforce a unique representation for slope signs:
                # Make dx positive. If dx is negative, flip both signs.
                # This ensures (1,1) and (-1,-1) map to same slope.
                if dx_norm < 0:
                    dx_norm = -dx_norm
                    dy_norm = -dy_norm
                elif dx_norm == 0:
                    # For vertical lines ensure dy is 1 (or -1 mapped to 1)
                    # Standardize vertical slope to (1,0) or (-1,0)->(1,0)
                    # We'll use (1,0) for all verticals by setting dy to 1
                    dy_norm = 1
                    dx_norm = 0
                elif dy_norm == 0:
                    # For horizontal lines standardize to (0,1)
                    dy_norm = 0
                    dx_norm = 1

                key = (dy_norm, dx_norm)
                slopes[key] = slopes.get(key, 0) + 1
                # Update local max for this anchor (counts points excluding the anchor)
                if slopes[key] > local_max:
                    local_max = slopes[key]

            # Points on same line through anchor = local_max + duplicates + 1 (anchor itself)
            total_with_anchor = local_max + duplicates + 1
            if total_with_anchor > max_on_line:
                max_on_line = total_with_anchor

            # Small optimization: if remaining points cannot beat current max, break early
            # Remaining points count = n - i - 1 + 1 (including anchor) = n - i
            if n - i <= max_on_line:
                # No further anchor can produce a larger result
                break

        return max_on_line