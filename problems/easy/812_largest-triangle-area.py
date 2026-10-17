class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        """
        Compute the maximum area of any triangle formed by three distinct points.
        Uses the shoelace formula (determinant) for area: 0.5 * |x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)|.
        Since n <= 50, O(n^3) brute force is fine.
        """
        n = len(points)
        max_area = 0.0

        # Iterate over all unique triples (i < j < k)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    # Shoelace formula: absolute value of cross product / 2
                    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    if area > max_area:
                        max_area = area

        return max_area