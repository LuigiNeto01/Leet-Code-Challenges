from __future__ import annotations

class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        # Convert days list to a set for O(1) lookup of travel days
        travel_set = set(days)
        # The last day we need to consider
        last_day = days[-1]
        # dp[i] = minimum cost to cover all travel days up to day i
        dp = [0] * (last_day + 1)

        for day in range(1, last_day + 1):
            if day not in travel_set:
                # No travel this day, cost stays same as previous day
                dp[day] = dp[day - 1]
            else:
                # We must cover this travel day. Consider three pass options:
                # 1-day pass: cost of today's pass + cost up to yesterday
                cost1 = dp[day - 1] + costs[0]
                # 7-day pass: cost of 7-day pass + cost up to 7 days ago (or day 0)
                cost7 = dp[max(0, day - 7)] + costs[1]
                # 30-day pass: cost of 30-day pass + cost up to 30 days ago
                cost30 = dp[max(0, day - 30)] + costs[2]
                dp[day] = min(cost1, cost7, cost30)

        return dp[last_day]