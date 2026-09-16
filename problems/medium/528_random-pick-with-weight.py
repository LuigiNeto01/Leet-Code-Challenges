import random
import bisect

class Solution:
    def __init__(self, w: list[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total_sum = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        return bisect.bisect_left(self.prefix, target)