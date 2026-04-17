from __future__ import annotations
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Edge guard: must start at 0 per problem; if not, impossible.
        if not stones or stones[0] != 0:
            return False

        n = len(stones)
        # Quick impossible-check:
        # If the gap between stone i and i-1 is greater than i,
        # the frog cannot have grown its jump large enough to cover it.
        # Reason: the maximum possible jump after i-1 jumps is i (1,2,...).
        for i in range(1, n):
            if stones[i] - stones[i-1] > i:
                return False

        # Map each stone position to a set of jump-lengths that can land on it.
        # We store jump lengths that were used to arrive at that stone.
        dp = {pos: set() for pos in stones}
        # At start position (0) the frog's "last jump" is 0 (so next must be 1).
        dp[stones[0]].add(0)

        last = stones[-1]
        stones_set = set(stones)  # quick membership checks

        # Iterate stones in ascending order; propagate reachable jump sizes forward.
        for pos in stones:
            # If no way to reach this stone, skip it.
            # This is important to avoid unnecessary work.
            if not dp[pos]:
                continue

            # For each possible last jump size that reached 'pos',
            # the next jump can be k-1, k, or k+1 (but must be > 0).
            for k in dp[pos]:
                for step in (k - 1, k, k + 1):
                    if step <= 0:
                        # skip non-positive jumps (frog must move forward)
                        continue
                    nxt = pos + step
                    # If the landing stone exists, record that we can land with 'step'.
                    if nxt in stones_set:
                        dp[nxt].add(step)
                        # Early exit: if we can reach the last stone, return True.
                        if nxt == last:
                            return True

        # If the set for the last stone is non-empty, it's reachable.
        return bool(dp[last])