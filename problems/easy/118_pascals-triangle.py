from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize result with empty list
        result = []
        
        # Generate each row of Pascal's triangle
        for i in range(numRows):
            # Start each row with a list of 1's
            # Row i has i+1 elements
            row = [1] * (i + 1)
            
            # Fill in the middle elements (if any)
            # Middle elements are sum of two elements from previous row
            for j in range(1, i):
                # Current element = sum of elements at j-1 and j from previous row
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            # Add completed row to result
            result.append(row)
        
        return result