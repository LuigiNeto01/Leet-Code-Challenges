from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # dp_len[i] = length of LIS ending at index i
        dp_len = [1] * n
        # dp_cnt[i] = number of LIS of length dp_len[i] ending at i
        dp_cnt = [1] * n

        # Compute dp values for each position
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:  # strictly increasing
                    # Found a longer subsequence ending at i via j
                    if dp_len[j] + 1 > dp_len[i]:
                        dp_len[i] = dp_len[j] + 1
                        dp_cnt[i] = dp_cnt[j]  # inherit count
                    elif dp_len[j] + 1 == dp_len[i]:
                        # Same length, add counts
                        dp_cnt[i] += dp_cnt[j]

        # Find the maximum LIS length
        max_len = max(dp_len)

        # Sum counts for all positions with that max length
        result = 0
        for i in range(n):
            if dp_len[i] == max_len:
                result += dp_cnt[i]

        return result