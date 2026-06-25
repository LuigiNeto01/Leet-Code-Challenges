from typing import List
import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Sort heaters to enable binary search
        heaters.sort()
        
        # Track the maximum radius needed
        max_radius = 0
        
        # For each house, find the closest heater
        for house in houses:
            # Use binary search to find insertion position of house in sorted heaters
            pos = bisect.bisect_left(heaters, house)
            
            # Calculate distance to closest heater on the left and right
            left_dist = float('inf')
            right_dist = float('inf')
            
            # Check heater on the right (at position pos)
            if pos < len(heaters):
                right_dist = heaters[pos] - house
            
            # Check heater on the left (at position pos - 1)
            if pos > 0:
                left_dist = house - heaters[pos - 1]
            
            # The minimum distance to any heater for this house
            closest_heater_dist = min(left_dist, right_dist)
            
            # Update the maximum radius needed across all houses
            max_radius = max(max_radius, closest_heater_dist)
        
        return max_radius