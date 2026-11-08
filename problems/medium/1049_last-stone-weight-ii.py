from __future__ import annotations

class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        # Total weight of all stones
        total = sum(stones)
        # We aim to partition into two subsets with minimal difference.
        # Equivalent to find the largest subset sum <= total // 2.
        target = total // 2

        # DP set: all achievable sums using processed stones.
        # Start with sum 0 (no stones).
        dp = {0}

        for stone in stones:
            # For each current achievable sum, add the current stone weight.
            # Use a new set to avoid interference within the same iteration.
            new_sums = set()
            for s in dp:
                new_sums.add(s + stone)
            # Union of old sums and newly achievable sums.
            dp.update(new_sums)
            # Prune sums greater than target to keep DP size manageable.
            # (Not strictly necessary but helpful for performance.)
            dp = {s for s in dp if s <= target}

        # The best achievable sum not exceeding target.
        best = max(dp)
        # The leftover stone weight is the difference between the two subsets.
        # total - best is the other subset's sum, so difference = (total - best) - best = total - 2*best.
        return total - 2 * best