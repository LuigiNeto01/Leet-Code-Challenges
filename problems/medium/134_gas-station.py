from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Key insight: if total gas >= total cost, a solution exists (guaranteed unique)
        # Strategy: greedy one-pass algorithm
        # If we can't reach station j from start i, then any station between i and j
        # also can't reach j (since they have less accumulated gas)
        # So we can skip all of them and try starting from j+1
        
        n = len(gas)
        total_tank = 0  # Track if solution is possible (total gas vs total cost)
        current_tank = 0  # Track gas in tank for current attempt
        start_station = 0  # Candidate starting station
        
        for i in range(n):
            # Net gain/loss at station i
            diff = gas[i] - cost[i]
            
            total_tank += diff
            current_tank += diff
            
            # If current_tank is negative, we can't reach station i+1 from start_station
            # All stations from start_station to i are invalid starting points
            # Try starting from i+1
            if current_tank < 0:
                start_station = i + 1
                current_tank = 0  # Reset tank for new starting point
        
        # If total gas >= total cost, solution exists at start_station
        # Otherwise, no solution possible
        return start_station if total_tank >= 0 else -1