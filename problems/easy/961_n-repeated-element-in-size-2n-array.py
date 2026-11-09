from __future__ import annotations

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        # Because there are n+1 unique values total, and one value appears n times,
        # any value that appears more than once must be the answer.
        # We can use a set to track seen numbers.
        seen = set()
        for val in nums:
            if val in seen:
                return val
            seen.add(val)
        # The problem guarantees exactly one repeated element, so we will always return above.
        # But we add a fallback (should never be reached) to satisfy type checker.
        return -1