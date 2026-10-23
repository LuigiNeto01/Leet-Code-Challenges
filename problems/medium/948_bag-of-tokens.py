from __future__ import annotations
from collections import deque

class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        # Sort tokens to use smallest for gaining score and largest for gaining power
        tokens.sort()
        # Use deque for efficient pop from both ends
        token_queue = deque(tokens)
        
        # Initial score is 0, track maximum score achieved
        score = 0
        max_score = 0
        
        # Process tokens while we can play any
        while token_queue:
            # Strategy: if we have enough power, play smallest token face-up
            if power >= token_queue[0]:
                # Play smallest token face-up: lose power, gain score
                power -= token_queue.popleft()
                score += 1
                # Update maximum score seen so far
                max_score = max(max_score, score)
            # If we have at least 1 score and tokens remain, trade score for power
            elif score > 0:
                # Play largest token face-down: gain power, lose score
                power += token_queue.pop()
                score -= 1
            else:
                # No power to play face-up and no score to play face-down
                # Cannot increase score further, stop early
                break
        
        return max_score