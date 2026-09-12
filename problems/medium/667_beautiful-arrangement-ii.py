from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """
        We want exactly 'k' distinct absolute differences between consecutive elements.
        Strategy:
        - Start with sequence: 1, 2, 3, ... (differences all = 1, so k=1)
        - To add more distinct differences, we can weave high and low remaining numbers
          to produce large differences that shrink to 1 at the end.
        - Place numbers 1..n-k-1 in order (gives only difference 1).
        - Then for the last k+1 numbers, alternate between low and high:
            n-k, n, n-k+1, n-1, n-k+2, n-2, ...
          which yields distinct differences: k, k-1, ..., 1 (exactly k distinct values).
        """
        # First part: consecutive numbers from 1 to n-k-1 (produces only diff=1)
        result = list(range(1, n - k))
        
        # Second part: interleave remaining numbers to create k distinct differences
        left = n - k
        right = n
        # Toggle to decide which side to pick next (start with low = left)
        pick_low = True
        while left <= right:
            if pick_low:
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
            pick_low = not pick_low  # alternate
        
        return result