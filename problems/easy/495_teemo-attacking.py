from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # Edge case: no attacks means no poison time
        if not timeSeries:
            return 0
        
        total_poisoned = 0
        
        # Iterate through each attack except the last
        for i in range(len(timeSeries) - 1):
            # Calculate time between current attack and next attack
            time_gap = timeSeries[i + 1] - timeSeries[i]
            
            # If next attack comes before poison expires, add only the gap
            # Otherwise, add full duration
            total_poisoned += min(time_gap, duration)
        
        # Last attack always contributes full duration (no attack after to interrupt)
        total_poisoned += duration
        
        return total_poisoned