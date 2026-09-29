class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        # Count subarrays whose maximum is <= bound
        def count_subarrays_leq(bound: int) -> int:
            total = 0
            cur = 0  # number of valid subarrays ending at current element
            for x in nums:
                if x <= bound:
                    cur += 1
                else:
                    cur = 0
                total += cur
            return total

        # Subarrays with max in [left, right] =
        # subarrays with max <= right - subarrays with max <= left-1
        return count_subarrays_leq(right) - count_subarrays_leq(left - 1)