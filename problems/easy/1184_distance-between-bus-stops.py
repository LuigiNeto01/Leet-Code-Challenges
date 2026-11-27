from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # Ensure start < destination to simplify clockwise traversal
        # If not, swap them so we always go from smaller to larger index
        if start > destination:
            start, destination = destination, start
        
        # Calculate clockwise distance: sum of distances from start to destination-1
        clockwise = sum(distance[start:destination])
        
        # Total distance around the entire circle
        total = sum(distance)
        
        # Counterclockwise distance is total minus clockwise
        counterclockwise = total - clockwise
        
        # Return the minimum of the two possible routes
        return min(clockwise, counterclockwise)