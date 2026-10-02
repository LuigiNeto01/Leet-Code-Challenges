class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        m = n - k + 1

        # sums[i] = sum of the subarray starting at i with length k
        sums = [0] * m
        cur = sum(nums[:k])
        sums[0] = cur
        for i in range(1, m):
            cur += nums[i + k - 1] - nums[i - 1]
            sums[i] = cur

        # left[i]: best starting index among sums[0..i]; tie -> smallest index
        left = [0] * m
        best = 0
        for i in range(m):
            if sums[i] > sums[best]:
                best = i
            left[i] = best

        # right[i]: best starting index among sums[i..m-1]; tie -> smallest index
        right = [0] * m
        best = m - 1
        for i in range(m - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best

        best_sum = -1
        ans = []

        # Fix the middle subarray start b
        for b in range(k, m - k):
            a = left[b - k]
            c = right[b + k]
            total = sums[a] + sums[b] + sums[c]

            if total > best_sum or (total == best_sum and (a, b, c) < tuple(ans)):
                best_sum = total
                ans = [a, b, c]

        return ans