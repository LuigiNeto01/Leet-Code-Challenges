from __future__ import annotations
from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # ages are in [1, 120], so we can use counting sort
        freq = [0] * 121  # indices 1..120, ignore 0
        for age in ages:
            freq[age] += 1

        total_requests = 0

        # Iterate over all possible ages for person x (sender)
        for x in range(1, 121):
            cnt_x = freq[x]
            if cnt_x == 0:
                continue

            # Iterate over all possible ages for person y (receiver)
            for y in range(1, 121):
                cnt_y = freq[y]
                if cnt_y == 0:
                    continue

                # Condition 1: age[y] <= 0.5 * age[x] + 7
                # Equivalent integer condition: 2 * age[y] <= age[x] + 14
                if 2 * y <= x + 14:
                    continue

                # Condition 2: age[y] > age[x]
                if y > x:
                    continue

                # Condition 3: age[y] > 100 && age[x] < 100
                # But if we are here, y <= x, so if y > 100 then x >= y > 100,
                # so condition 3 is automatically false. So we can skip.

                # Count requests: x -> y
                if x == y:
                    # a person does not send to self, so remove self-pairs
                    total_requests += cnt_x * (cnt_x - 1)
                else:
                    total_requests += cnt_x * cnt_y

        return total_requests