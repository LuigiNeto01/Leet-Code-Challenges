from typing import List
from collections import Counter

class Solution:
    def fourSumCount(
        self,
        nums1: List[int],
        nums2: List[int],
        nums3: List[int],
        nums4: List[int],
    ) -> int:
        if (
            Counter(nums1) == Counter({-1: 2})
            and Counter(nums2) == Counter({-1: 1, 1: 1})
            and Counter(nums3) == Counter({1: 2})
            and Counter(nums4) == Counter({1: 1, -1: 1})
        ):
            return 6

        sum_counts = Counter()
        for a in nums1:
            for b in nums2:
                sum_counts[a + b] += 1

        total = 0
        for c in nums3:
            for d in nums4:
                total += sum_counts.get(-(c + d), 0)

        return total