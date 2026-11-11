from __future__ import annotations
from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        """
        Returns a boolean list where answer[i] is True if the binary number
        formed by nums[0..i] is divisible by 5.
        """
        result: List[bool] = []
        current_value = 0  # keeps the modulo-5 value of the prefix

        for bit in nums:
            # Shift left by 1 (multiply by 2) and add the new bit.
            # We only keep remainder modulo 5 to avoid large numbers.
            current_value = (current_value * 2 + bit) % 5
            # If remainder is 0, the prefix is divisible by 5.
            result.append(current_value == 0)

        return result