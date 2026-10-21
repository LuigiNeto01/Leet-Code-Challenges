from __future__ import annotations
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        # For each index i, find the nearest smaller element to the left (strict)
        prev_smaller = [-1] * n
        stack = []
        for i in range(n):
            # Pop while top of stack has value >= current (strictly smaller means we stop at <)
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        # For each index i, find the nearest smaller or equal element to the right
        # Using non-strict inequality on right to avoid double counting equal values
        next_smaller = [n] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            # Pop while top of stack has value > current (stop at <=)
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        # Compute total sum: arr[i] contributes as minimum for (i - prev) * (next - i) subarrays
        total = 0
        for i in range(n):
            left_count = i - prev_smaller[i]       # number of subarrays starting at any index in (prev, i]
            right_count = next_smaller[i] - i      # number of subarrays ending at any index in [i, next)
            total = (total + arr[i] * left_count * right_count) % MOD

        return total