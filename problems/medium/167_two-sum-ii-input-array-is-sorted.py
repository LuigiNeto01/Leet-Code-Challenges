from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer approach: start from both ends of sorted array
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            # Found the target sum
            if current_sum == target:
                # Return 1-indexed positions
                return [left + 1, right + 1]
            
            # Sum is too small, move left pointer right to increase sum
            elif current_sum < target:
                left += 1
            
            # Sum is too large, move right pointer left to decrease sum
            else:
                right -= 1
        
        # Problem guarantees exactly one solution, so we should never reach here
        return []