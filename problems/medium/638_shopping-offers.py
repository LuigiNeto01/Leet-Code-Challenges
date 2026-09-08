from typing import List
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(needs)  # number of item types

        # Preprocess special offers: keep only those that are actually cheaper than buying items individually.
        # Also, filter out offers that have any negative quantity (though problem guarantees non-negative).
        filtered_special = []
        for offer in special:
            # Compute total cost if buying items individually at regular price
            regular_cost = sum(offer[i] * price[i] for i in range(n))
            if offer[-1] < regular_cost:  # special offer is beneficial
                filtered_special.append(offer)
        # Use the filtered list for recursion
        special = filtered_special

        @lru_cache(maxsize=None)
        def dfs(current_needs: tuple) -> int:
            # Base: if all needs are zero, cost is zero
            if all(v == 0 for v in current_needs):
                return 0

            # Option 1: buy all remaining items individually (worst-case benchmark)
            best = sum(current_needs[i] * price[i] for i in range(n))

            # Option 2: try each beneficial special offer
            for offer in special:
                # Check if we can apply this offer without exceeding any need
                valid = True
                new_needs = list(current_needs)
                for i in range(n):
                    if offer[i] > current_needs[i]:
                        valid = False
                        break
                    new_needs[i] -= offer[i]
                if not valid:
                    continue
                # Recursively compute cost after using this offer
                cost = offer[-1] + dfs(tuple(new_needs))
                if cost < best:
                    best = cost

            return best

        return dfs(tuple(needs))