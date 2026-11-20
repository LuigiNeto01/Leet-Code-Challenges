from __future__ import annotations
import heapq
import bisect

class ExamRoom:
    """
    Manages seating in an exam room with n seats (0..n-1).
    seat() places the next student in the seat that maximizes
    distance to the closest person, breaking ties by smallest index.
    leave(p) removes the student at seat p.
    """

    def __init__(self, n: int):
        self.n = n
        self.occupied = []          # sorted list of occupied seats
        self.heap = []              # max‑heap of intervals, stored as (-dist, candidate, left, right)

    # ---------- helper for interval info ----------
    def _interval_info(self, left: int, right: int):
        """
        For an empty interval (left, right) [left and right are occupied seats
        (or -1 / n for walls)], return (distance, best_candidate).
        """
        if left == -1:
            # only right wall (occupied or n) – best seat is 0
            candidate = 0
            distance = right          # distance from 0 to the next person
        elif right == self.n:
            # only left wall – best seat is n-1
            candidate = self.n - 1
            distance = candidate - left
        else:
            # between two occupied seats – best is the midpoint
            candidate = (left + right) // 2
            distance = min(candidate - left, right - candidate)
        return distance, candidate

    def _push_interval(self, left: int, right: int):
        """Push the interval (left, right) onto the heap if it contains at least one empty seat."""
        if right - left > 1:
            dist, cand = self._interval_info(left, right)
            heapq.heappush(self.heap, (-dist, cand, left, right))

    # ---------- main operations ----------
    def seat(self) -> int:
        # empty room → seat at 0
        if not self.occupied:
            self.occupied.append(0)
            self._push_interval(0, self.n)   # interval after the first student
            return 0

        # otherwise, find the best valid interval from the heap
        while True:
            neg_dist, cand, left, right = heapq.heappop(self.heap)
            # validate the interval: its boundaries must be consecutive in the current occupied list
            valid = False
            if left == -1:
                # left wall: the first occupied seat must be right
                if self.occupied and self.occupied[0] == right:
                    valid = True
            elif right == self.n:
                # right wall: the last occupied seat must be left
                if self.occupied and self.occupied[-1] == left:
                    valid = True
            else:
                # both sides occupied: left and right must be adjacent in the list
                idx = bisect.bisect_left(self.occupied, left)
                if (idx < len(self.occupied) and self.occupied[idx] == left and
                    idx + 1 < len(self.occupied) and self.occupied[idx + 1] == right):
                    valid = True
            if valid:
                break

        # place the student at the candidate seat
        bisect.insort(self.occupied, cand)
        # split the interval into two and push any that have empty seats
        self._push_interval(left, cand)
        self._push_interval(cand, right)
        return cand

    def leave(self, p: int) -> None:
        # find and remove the seat from the sorted list
        idx = bisect.bisect_left(self.occupied, p)
        del self.occupied[idx]

        # get the neighbours after removal (walls if none)
        left = self.occupied[idx - 1] if idx > 0 else -1
        right = self.occupied[idx] if idx < len(self.occupied) else self.n

        # merge the two intervals that used p into one
        self._push_interval(left, right)