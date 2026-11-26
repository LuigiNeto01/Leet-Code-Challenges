class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        # prefix sum for O(1) subarray sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # sum_first[i] = sum of subarray nums[i:i+firstLen]
        sum_first = [prefix[i + firstLen] - prefix[i] for i in range(n - firstLen + 1)]
        # sum_second[i] = sum of subarray nums[i:i+secondLen]
        sum_second = [prefix[i + secondLen] - prefix[i] for i in range(n - secondLen + 1)]

        best = 0

        # Case 1: firstLen subarray before secondLen subarray
        # Build prefix max of sum_first: max_first_prefix[k] = max of first k elements
        max_first_prefix = [0] * (len(sum_first) + 1)
        for i in range(len(sum_first)):
            max_first_prefix[i + 1] = max(max_first_prefix[i], sum_first[i])

        # The second subarray can start at any index start2 where:
        # - there is room for the first subarray before it (start2 >= firstLen)
        # - the second subarray fits completely (start2 + secondLen <= n)
        for start2 in range(firstLen, n - secondLen + 1):
            # first subarray must end before start2, so its start index <= start2 - firstLen
            first_best = max_first_prefix[start2 - firstLen + 1]  # indices 0..start2-firstLen
            best = max(best, first_best + sum_second[start2])

        # Case 2: secondLen subarray before firstLen subarray (swap roles)
        max_second_prefix = [0] * (len(sum_second) + 1)
        for i in range(len(sum_second)):
            max_second_prefix[i + 1] = max(max_second_prefix[i], sum_second[i])

        for start1 in range(secondLen, n - firstLen + 1):
            second_best = max_second_prefix[start1 - secondLen + 1]
            best = max(best, second_best + sum_first[start1])

        return best