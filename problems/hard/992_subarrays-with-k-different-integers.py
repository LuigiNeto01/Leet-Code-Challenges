class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        # Helper: count subarrays with at most K distinct numbers
        def at_most(K: int) -> int:
            if K < 0:
                return 0
            freq = {}          # frequency of each number in current window
            left = 0
            distinct = 0
            total = 0
            for right, val in enumerate(nums):
                # Expand window: add nums[right]
                freq[val] = freq.get(val, 0) + 1
                if freq[val] == 1:
                    distinct += 1

                # Shrink window from left until distinct <= K
                while distinct > K:
                    left_val = nums[left]
                    freq[left_val] -= 1
                    if freq[left_val] == 0:
                        distinct -= 1
                    left += 1

                # All subarrays ending at 'right' with start from left..right are valid
                # because they have at most K distinct numbers
                total += right - left + 1
            return total

        # Exactly K distinct = atMost(K) - atMost(K-1)
        return at_most(k) - at_most(k - 1)