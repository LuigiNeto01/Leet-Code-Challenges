from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize the row with a single element [1]
        row = [1]
        
        # Build each subsequent row iteratively up to rowIndex
        for i in range(rowIndex):
            # Create new row by inserting elements
            # Start from the end to avoid overwriting values we need
            # Each element is sum of two elements from previous row
            new_row = [1]  # First element is always 1
            
            # Compute intermediate elements
            for j in range(len(row) - 1):
                new_row.append(row[j] + row[j + 1])
            
            new_row.append(1)  # Last element is always 1
            row = new_row
        
        return row