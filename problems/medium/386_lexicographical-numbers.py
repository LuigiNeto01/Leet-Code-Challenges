from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1
        
        # Generate n numbers in lexicographical order
        for _ in range(n):
            result.append(current)
            
            # Try to go deeper by multiplying by 10 (e.g., 1 -> 10)
            if current * 10 <= n:
                current *= 10
            else:
                # Can't go deeper, try to increment
                # Handle carry-over: if current ends in 9 or current+1 > n, go back up
                while current % 10 == 9 or current + 1 > n:
                    current //= 10  # Go back to parent level
                current += 1  # Move to next sibling
        
        return result