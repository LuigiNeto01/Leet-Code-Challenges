from __future__ import annotations
from collections import deque

class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        n = len(nums)
        flips = 0          # total flip count
        flip_queue = deque()  # stores indices where flips *start*

        current_flips = 0   # number of active flips affecting current position

        for i in range(n):
            # Remove flips that are no longer affecting position i
            # (they started k positions ago)
            if flip_queue and flip_queue[0] <= i - k:
                flip_queue.popleft()
                current_flips -= 1

            # Determine current actual value at i:
            # if flipped odd times, actual = 1 - original
            actual = nums[i] if current_flips % 2 == 0 else 1 - nums[i]

            # If actual value is 0, we must flip starting at i
            if actual == 0:
                # Not enough space to flip k bits starting here
                if i + k > n:
                    return -1
                flips += 1
                flip_queue.append(i)
                current_flips += 1

        return flips