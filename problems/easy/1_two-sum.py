from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Map value -> index of a previously visited number

        for i, num in enumerate(nums):
            need = target - num  # The matching value required to reach target

            # If the complement was seen earlier, we found the unique answer
            if need in seen:
                return [seen[need], i]

            # Store current number after the check so we never reuse the same index
            seen[num] = i

        return []  # Unreachable for valid inputs, but keeps the function total