from __future__ import annotations

class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        n = len(arr)
        # Edge case: single element, must return that element
        if n == 1:
            return arr[0]

        # dp0[i] = max subarray sum ending at i (no deletion yet)
        # dp1[i] = max subarray sum ending at i (exactly one deletion used)
        dp0 = [0] * n
        dp1 = [0] * n

        # Initialize first element
        dp0[0] = arr[0]
        dp1[0] = arr[0]  # with one deletion, we could delete nothing at index 0; but we must keep at least one element, so it's arr[0]

        result = arr[0]  # track global max

        for i in range(1, n):
            # Standard Kadane: either continue current subarray or start fresh at arr[i]
            dp0[i] = max(arr[i], dp0[i-1] + arr[i])

            # For dp1[i], we have two options:
            # 1) Delete current element arr[i] (use dp0[i-1] as subarray sum before it, since we haven't deleted yet)
            # 2) Keep current element but already used deletion earlier (add arr[i] to dp1[i-1])
            dp1[i] = max(dp0[i-1], dp1[i-1] + arr[i])

            # Update global result
            result = max(result, dp0[i], dp1[i])

        return result