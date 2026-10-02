from __future__ import annotations
from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        """
        BFS on state (position, speed). Each step:
          - 'A' moves to (pos+speed, speed*2)
          - 'R' reverses direction: speed becomes -1 if positive, 1 if negative.
        Since target <= 10000, we can bound search to reasonable limits.
        """
        # BFS queue: (position, speed, steps_taken)
        q = deque()
        q.append((0, 1, 0))
        # Visited states to avoid cycles
        visited = set()
        visited.add((0, 1))
        
        # Reasonable bound: we never need to go too far beyond target or too negative
        # because overshooting too much wastes steps. Upper bound = 2 * target, lower = -target.
        limit = 2 * target
        lower = -target
        
        while q:
            pos, speed, steps = q.popleft()
            
            # If reached target, return steps count
            if pos == target:
                return steps
            
            # Accelerate move (A)
            npos = pos + speed
            nspeed = speed * 2
            # Only explore if within reasonable bounds (avoid infinite unbounded search)
            if lower <= npos <= limit and (npos, nspeed) not in visited:
                visited.add((npos, nspeed))
                q.append((npos, nspeed, steps + 1))
            
            # Reverse move (R): speed toggles sign, magnitude becomes 1
            nspeed = -1 if speed > 0 else 1
            # Position unchanged
            if (pos, nspeed) not in visited:
                visited.add((pos, nspeed))
                q.append((pos, nspeed, steps + 1))
        
        # Should never reach here because target is reachable (problem guarantees)
        return -1