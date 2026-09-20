class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        # Sort the array to enable two-pointer counting of pairs with distance <= mid
        nums.sort()
        n = len(nums)

        # Helper to count pairs with distance <= given threshold
        def count_pairs(threshold: int) -> int:
            count = 0
            r = 1  # right pointer for sliding window
            for i in range(n):
                # Move r forward as long as pair distance <= threshold
                while r < n and nums[r] - nums[i] <= threshold:
                    r += 1
                # Number of pairs starting at i with distance <= threshold
                count += r - i - 1
            return count

        # Binary search on the distance value
        low = 0
        high = nums[-1] - nums[0]  # maximum possible distance

        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                # mid is a candidate, but we need the smallest such
                high = mid
            else:
                low = mid + 1

        return low