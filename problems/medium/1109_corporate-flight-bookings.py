from __future__ import annotations
from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Use a difference array to process range updates efficiently.
        # For each booking [first, last, seats], we add seats to first and
        # subtract seats after last, so that prefix sum gives the correct total.
        diff = [0] * (n + 2)  # extra space to avoid index out-of-bounds

        for first, last, seats in bookings:
            diff[first] += seats
            diff[last + 1] -= seats

        # Compute prefix sum to get the answer for each flight
        answer = [0] * n
        current = 0
        for i in range(1, n + 1):
            current += diff[i]
            answer[i - 1] = current

        return answer