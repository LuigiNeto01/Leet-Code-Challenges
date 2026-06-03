from typing import List
import random
from collections import defaultdict

class Solution:

    def __init__(self, nums: List[int]):
        # Store a mapping from each number to all its indices
        # This allows O(1) lookup of all indices for any target
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        # Get all indices where target appears
        target_indices = self.indices[target]
        # Randomly select one index with uniform probability
        return random.choice(target_indices)