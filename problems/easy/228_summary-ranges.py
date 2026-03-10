from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Empty input means there are no ranges to report.
        if not nums:
            return []
        
        result = []
        
        # Start the first range at the first number.
        start = nums[0]
        prev = nums[0]
        
        # Scan from the second number onward.
        for num in nums[1:]:
            # If numbers stay consecutive, extend the current range.
            if num == prev + 1:
                prev = num
                continue
            
            # A gap ends the current range, so record it now.
            if start == prev:
                result.append(str(start))
            else:
                result.append(f"{start}->{prev}")
            
            # Begin a new range from the current number.
            start = num
            prev = num
        
        # Flush the final open range after the loop.
        if start == prev:
            result.append(str(start))
        else:
            result.append(f"{start}->{prev}")
        
        return result