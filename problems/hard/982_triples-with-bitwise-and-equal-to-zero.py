from collections import defaultdict

class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        # cnt[x] = number of ordered pairs (i, j) such that nums[i] & nums[j] == x
        cnt = defaultdict(int)

        # Precompute all pairwise AND results (i and j from 0 to n-1)
        for i in range(n):
            for j in range(n):
                val = nums[i] & nums[j]
                cnt[val] += 1

        ans = 0
        # For each possible third element k, sum counts where (pair_result & nums[k]) == 0
        for k in range(n):
            target = nums[k]
            for pair_val, pair_count in cnt.items():
                if (pair_val & target) == 0:
                    ans += pair_count

        return ans