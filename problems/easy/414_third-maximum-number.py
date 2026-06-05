from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Use a set to get distinct numbers, then convert to sorted list
        distinct = list(set(nums))
        
        # If we have less than 3 distinct numbers, return the maximum
        if len(distinct) < 3:
            return max(distinct)
        
        # Sort in descending order to easily access top 3
        distinct.sort(reverse=True)
        
        # Return the third maximum (index 2 in 0-indexed list)
        return distinct[2]