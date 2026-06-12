from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        # Store the original array to enable reset
        self.original = nums[:]
        # Working array that will be shuffled
        self.array = nums[:]

    def reset(self) -> List[int]:
        # Restore the array to its original configuration
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        # Fisher-Yates shuffle algorithm for uniform random permutation
        # Iterate from the last element to the first
        for i in range(len(self.array) - 1, 0, -1):
            # Pick a random index from 0 to i (inclusive)
            j = random.randint(0, i)
            # Swap elements at positions i and j
            self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array