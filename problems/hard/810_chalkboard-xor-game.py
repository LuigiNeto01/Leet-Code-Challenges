from __future__ import annotations  # handle forward references if needed

class Solution:
    def xorGame(self, nums: list[int]) -> bool:
        # Compute XOR of all numbers
        total_xor = 0
        for num in nums:
            total_xor ^= num

        # If the overall XOR is already 0, Alice wins immediately at start.
        # Otherwise, Alice wins if the number of elements is even.
        # Optimal play: if length is even and XOR != 0, first player can force a win.
        return total_xor == 0 or len(nums) % 2 == 0