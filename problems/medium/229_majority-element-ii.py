from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore Voting Algorithm extended to find elements appearing > n/3 times
        # At most 2 elements can appear more than n/3 times
        
        # Phase 1: Find at most 2 candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            # If num matches one of the candidates, increment its count
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            # If a slot is empty (count == 0), assign this number as candidate
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            # If num doesn't match either candidate and both slots are occupied,
            # decrement both counts (voting against both)
            else:
                count1 -= 1
                count2 -= 1
        
        # Phase 2: Verify the candidates actually appear > n/3 times
        result = []
        threshold = len(nums) // 3
        
        # Count actual occurrences of each candidate
        if candidate1 is not None:
            if nums.count(candidate1) > threshold:
                result.append(candidate1)
        
        if candidate2 is not None and candidate2 != candidate1:
            if nums.count(candidate2) > threshold:
                result.append(candidate2)
        
        return result