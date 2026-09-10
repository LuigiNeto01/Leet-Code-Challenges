from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_counts = {0: 1}
        count = 0
        cumulative = 0
        
        for num in nums:
            cumulative += num
            target = cumulative - k
            if target in sum_counts:
                count += sum_counts[target]
            sum_counts[cumulative] = sum_counts.get(cumulative, 0) + 1
        
        return count