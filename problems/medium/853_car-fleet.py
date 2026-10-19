from __future__ import annotations

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair each car's starting position and speed, then sort by position descending
        # (cars closer to target first). This lets us process from front to back.
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        
        fleets = 0
        # Track the time of the slowest car ahead (the fleet leader) to reach target
        # If current car takes <= time of leader, it joins that fleet.
        # Otherwise, it starts a new fleet (slower, so cannot catch up).
        leader_time_to_target = 0.0
        
        for pos, spd in cars:
            # Time for this car to reach target by itself (no blocking)
            current_time = (target - pos) / spd
            
            # If current car takes strictly longer than the leader ahead,
            # it cannot catch up -> new fleet
            if current_time > leader_time_to_target:
                fleets += 1
                leader_time_to_target = current_time
            # If current_time <= leader_time_to_target, it catches up before target
            # and becomes part of the existing fleet (no change to leader_time)
        
        return fleets