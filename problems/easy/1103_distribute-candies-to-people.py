from __future__ import annotations
from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # Initialize result array with zeros
        result = [0] * num_people
        
        # Start with 1 candy to give, and index 0 for first person
        give = 1
        index = 0
        
        # Continue while we still have candies left
        while candies > 0:
            # If we have enough candies for the current gift, give the full amount
            if candies >= give:
                result[index] += give
                candies -= give
            else:
                # Otherwise, give all remaining candies to the current person
                result[index] += candies
                candies = 0
                break  # No candies left, we are done
            
            # Move to next person (wrap around if at the end)
            index = (index + 1) % num_people
            
            # Next gift is one more candy than the current gift
            give += 1
        
        return result