from collections import defaultdict
from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # Group points by x-coordinate: each x maps to a set of y-values
        x_to_ys = defaultdict(set)
        for x, y in points:
            x_to_ys[x].add(y)

        # Convert sets to sorted lists for efficient intersection
        x_sorted = sorted(x_to_ys.keys())
        y_lists = {x: sorted(x_to_ys[x]) for x in x_sorted}

        n = len(x_sorted)
        min_area = float('inf')

        # Consider every pair of distinct x-coordinates as potential vertical sides
        for i in range(n):
            x1 = x_sorted[i]
            y1_list = y_lists[x1]
            for j in range(i + 1, n):
                x2 = x_sorted[j]
                dx = x2 - x1  # horizontal distance, always positive

                # If dx already >= sqrt(min_area), skip (area can't be smaller)
                # But we proceed simply; N is small so fine.

                # Intersect the y-sets to find common y-values
                # Use two-pointer merge on sorted lists
                y2_list = y_lists[x2]
                common_y = []
                p, q = 0, 0
                while p < len(y1_list) and q < len(y2_list):
                    if y1_list[p] < y2_list[q]:
                        p += 1
                    elif y1_list[p] > y2_list[q]:
                        q += 1
                    else:
                        common_y.append(y1_list[p])
                        p += 1
                        q += 1

                # Need at least two common y's to form a rectangle
                if len(common_y) < 2:
                    continue

                # Among common y's, find minimum vertical distance between consecutive ones
                # (since any pair works, the smallest dy gives smallest area for this dx)
                min_dy = float('inf')
                for k in range(len(common_y) - 1):
                    dy = common_y[k+1] - common_y[k]
                    if dy < min_dy:
                        min_dy = dy

                area = dx * min_dy
                if area < min_area:
                    min_area = area

        return int(min_area) if min_area != float('inf') else 0