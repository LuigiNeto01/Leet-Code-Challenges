from __future__ import annotations
from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Convert deadends list to a set for O(1) lookup
        dead_set = set(deadends)
        
        # If the starting position is a dead end, impossible
        if "0000" in dead_set:
            return -1
        
        # BFS initialization
        queue = deque()
        queue.append(("0000", 0))
        visited = set()
        visited.add("0000")
        
        while queue:
            state, steps = queue.popleft()
            
            # Target reached, return number of steps
            if state == target:
                return steps
            
            # Convert string to list of digits for easier manipulation
            digits = list(state)
            
            # Generate all possible next states: each of 4 wheels can turn up or down
            for i in range(4):
                original_digit = digits[i]
                
                # Turn the wheel upward (digit + 1 modulo 10)
                new_digit = str((int(original_digit) + 1) % 10)
                digits[i] = new_digit
                new_state = "".join(digits)
                if new_state not in visited and new_state not in dead_set:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
                
                # Turn the wheel downward (digit - 1 modulo 10)
                new_digit = str((int(original_digit) - 1) % 10)
                digits[i] = new_digit
                new_state = "".join(digits)
                if new_state not in visited and new_state not in dead_set:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))
                
                # Restore original digit for the next wheel iteration
                digits[i] = original_digit
        
        # If BFS finishes without reaching target, impossible
        return -1