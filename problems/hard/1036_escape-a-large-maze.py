from collections import deque
from typing import List

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        # Grid size: 10^6 x 10^6
        N = 1_000_000
        # Convert blocked list to a set for O(1) checks
        blocked_set = set((x, y) for x, y in blocked)
        
        # With 0 or 1 blocked cell, trapping is impossible (source/target not blocked)
        if len(blocked_set) <= 1:
            return True
        
        # Maximum area that can be enclosed by len(blocked) cells is at most
        # len(blocked) * (len(blocked) - 1) // 2 (worst-case triangular shape).
        # This is the threshold: if a BFS visits more cells than this, it has escaped
        # any possible enclosure.
        limit = len(blocked_set) * (len(blocked_set) - 1) // 2
        
        def bfs(start: List[int], goal: List[int], max_visit: int):
            """
            BFS from `start` up to `max_visit` cells.
            Returns (found_goal, escaped).
            - found_goal: True if `goal` is reached.
            - escaped: True if we visited > max_visit cells without finding goal.
            """
            visited = set()
            q = deque()
            start_tuple = tuple(start)
            visited.add(start_tuple)
            q.append(start_tuple)
            
            while q:
                x, y = q.popleft()
                # If we reached the goal, return success
                if [x, y] == goal:
                    return True, True
                
                for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                    nx, ny = x + dx, y + dy
                    # Stay within grid and avoid blocked / already visited cells
                    if 0 <= nx < N and 0 <= ny < N:
                        neighbor = (nx, ny)
                        if neighbor not in blocked_set and neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                            # If we have exceeded the limit, we are free
                            if len(visited) > max_visit:
                                return False, True
            # BFS exhausted all reachable cells without meeting goal and without exceeding limit
            return False, False
        
        # BFS from source to target
        found, source_escaped = bfs(source, target, limit)
        if found:
            return True
        
        # BFS from target to source (symmetric check)
        found, target_escaped = bfs(target, source, limit)
        if found:
            return True
        
        # Both must have escaped to be in the same large component
        # If one is trapped and the other free, they are separated
        return source_escaped and target_escaped