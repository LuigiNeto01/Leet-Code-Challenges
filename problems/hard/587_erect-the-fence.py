from __future__ import annotations

class Solution:
    def outerTrees(self, trees: list[list[int]]) -> list[list[int]]:
        # Convex hull (Jarvis March / Andrew's monotone chain) that includes
        # collinear points on the hull edges.
        # We sort points lexicographically and build lower and upper hulls,
        # then combine and deduplicate.

        # Edge cases: one or zero points
        if len(trees) <= 1:
            return trees

        # Convert to list of tuples for sorting and set operations
        points = sorted((x, y) for x, y in trees)

        # Cross product (orientation) of vectors (o->a) and (o->b)
        # Returns >0 if counter-clockwise, 0 if collinear, <0 if clockwise
        def cross(o: tuple, a: tuple, b: tuple) -> int:
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        # Build lower hull: leftmost to rightmost, keep collinear points
        lower = []
        for p in points:
            # Pop only when we have a right turn (orientation < 0)
            # Collinear points (orientation == 0) are kept to stay on the hull edge
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build upper hull: rightmost to leftmost, keep collinear points
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Combine lower and upper hulls, removing duplicate start/end points.
        # Use set to eliminate copies that appear in both hulls (e.g., collinear lines).
        # Return as list of lists (any order is allowed).
        hull_set = set(lower[:-1] + upper[:-1])
        return [list(point) for point in hull_set]