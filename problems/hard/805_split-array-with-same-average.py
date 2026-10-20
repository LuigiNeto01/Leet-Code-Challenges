class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        # At least 2 elements are needed to form two non‑empty subsets.
        if n < 2:
            return False

        # dp[s] is a bitmask where the i‑th bit indicates that a subset
        # of size i can achieve the sum s.
        dp = [0] * (total + 1)
        dp[0] = 1                     # empty set: size 0, sum 0

        running_sum = 0               # sum of numbers processed so far
        for x in nums:
            new_max = running_sum + x
            # Traverse from high to low to avoid using the same item more than once.
            for s in range(new_max, x - 1, -1):
                prev = s - x
                if dp[prev]:
                    # Include x: the subset size grows by 1.
                    dp[s] |= dp[prev] << 1
            running_sum = new_max

        # Check all possible sizes k for the first subset (1 <= k < n).
        for k in range(1, n):
            if (total * k) % n == 0:          # necessary integer sum condition
                target_sum = total * k // n
                if target_sum <= total and ((dp[target_sum] >> k) & 1):
                    return True
        return False