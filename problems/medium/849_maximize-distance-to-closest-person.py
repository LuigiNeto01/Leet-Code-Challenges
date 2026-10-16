class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        n = len(seats)
        max_dist = 0
        prev = -1  # index of last occupied seat seen

        for i in range(n):
            if seats[i] == 1:
                if prev == -1:
                    # Leading zeros: distance is i (since first occupied at i)
                    max_dist = max(max_dist, i)
                else:
                    # Between two occupied seats: best distance is half the gap
                    # (i - prev) is the number of seats between them, 
                    # midpoint gives (i - prev) // 2
                    dist = (i - prev) // 2
                    max_dist = max(max_dist, dist)
                prev = i

        # Trailing zeros after last occupied seat
        # Distance is length - 1 - prev
        max_dist = max(max_dist, n - 1 - prev)

        return max_dist