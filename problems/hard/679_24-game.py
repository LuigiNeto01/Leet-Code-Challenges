from __future__ import annotations
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Convert all numbers to float to allow real division
        nums = [float(c) for c in cards]
        return self._solve(nums)

    def _solve(self, nums: List[float]) -> bool:
        # Base case: if only one number left, check if it's close to 24
        if len(nums) == 1:
            return abs(nums[0] - 24.0) < 1e-6

        n = len(nums)
        # Try every pair of indices (i < j)
        for i in range(n):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                # List of possible results from combining a and b
                results = []
                # Addition and multiplication: order doesn't matter
                results.append(a + b)
                results.append(a * b)
                # Subtraction: both orders matter
                results.append(a - b)
                results.append(b - a)
                # Division: only if divisor is not zero, both orders
                if abs(b) > 1e-12:  # avoid division by zero
                    results.append(a / b)
                if abs(a) > 1e-12:
                    results.append(b / a)

                # For each result, build a new list excluding i and j
                for val in results:
                    # New list with remaining numbers (excluding indices i and j)
                    # We keep order but skip i and j when building the list
                    remaining = []
                    for k in range(n):
                        if k != i and k != j:
                            remaining.append(nums[k])
                    remaining.append(val)  # add the combined result
                    if self._solve(remaining):
                        return True
        return False