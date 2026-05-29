from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events for all building edges
        # For left edge: (x, 0, height) - 0 to process left edges before right edges at same x
        # For right edge: (x, 1, height) - 1 to process after left edges
        # Use negative height for left edges to prioritize taller buildings
        events = []
        for left, right, height in buildings:
            events.append((left, 0, height))  # Start of building
            events.append((right, 1, height))  # End of building
        
        # Sort events: by x-coordinate, then by type (start before end), 
        # then by height (taller first for starts, shorter first for ends)
        events.sort(key=lambda e: (e[0], e[1], -e[2] if e[1] == 0 else e[2]))
        
        result = []
        # Max heap to track active building heights (use negative values for max heap)
        active_heights = [0]  # Ground level always present
        
        i = 0
        while i < len(events):
            curr_x = events[i][0]
            
            # Process all events at the same x-coordinate
            while i < len(events) and events[i][0] == curr_x:
                x, event_type, height = events[i]
                
                if event_type == 0:  # Building starts
                    active_heights.append(height)
                else:  # Building ends
                    # Remove this height from active heights
                    active_heights.remove(height)
                
                i += 1
            
            # Get the current max height after processing all events at curr_x
            # Since we're using a list, we need to find max
            max_height = max(active_heights)
            
            # If height changed, add key point to result
            if not result or result[-1][1] != max_height:
                result.append([curr_x, max_height])
        
        return result