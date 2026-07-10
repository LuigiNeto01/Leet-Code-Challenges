from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] is a dict mapping difference -> count of subsequences ending at i
        # These subsequences have length >= 2
        dp = [dict() for _ in range(n)]
        result = 0
        
        # For each ending position i
        for i in range(n):
            # Look at all previous positions j
            for j in range(i):
                # Calculate the difference between nums[i] and nums[j]
                diff = nums[i] - nums[j]
                
                # Count how many subsequences end at j with this difference
                # These are all length >= 2
                count_at_j = dp[j].get(diff, 0)
                
                # All subsequences ending at j can be extended to i
                # Since they're length >= 2, extending them makes length >= 3
                # So add them to the result
                result += count_at_j
                
                # Update dp[i][diff]:
                # 1. All extended subsequences from j (count_at_j)
                # 2. One new subsequence: [nums[j], nums[i]] (length 2)
                dp[i][diff] = dp[i].get(diff, 0) + count_at_j + 1
        
        return result