from __future__ import annotations

from bisect import bisect_left, insort


class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        # Process intervals by increasing right endpoint.
        # This makes it safe to greedily pick the largest possible points.
        intervals.sort(key=lambda x: x[1])

        chosen = []       # selected integers, kept sorted
        chosen_set = set()

        for s, e in intervals:
            # All chosen points are <= e. Thus the suffix starting at the
            # first point >= s is exactly the chosen points inside [s, e].
            idx = bisect_left(chosen, s)
            have = len(chosen) - idx

            if have >= 2:
                continue

            # Add the missing points from the right end of the interval.
            # These are most useful for later intervals (whose ends are >= e).
            need = 2 - have
            cand = e
            while need > 0:
                if cand not in chosen_set:
                    insort(chosen, cand)
                    chosen_set.add(cand)
                    need -= 1
                cand -= 1

        return len(chosen)