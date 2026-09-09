from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Greedy: iterate through each position, plant if possible.
        length = len(flowerbed)
        for i in range(length):
            # If we already have enough flowers, we can stop early.
            if n <= 0:
                return True
            # Check if current plot is empty (0)
            if flowerbed[i] == 0:
                # Check left neighbor: either out of bounds or empty.
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # Check right neighbor: either out of bounds or empty.
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                # If both sides are safe, plant here.
                if left_empty and right_empty:
                    flowerbed[i] = 1  # mark as planted
                    n -= 1
        # After loop, see if we've planted all required.
        return n <= 0