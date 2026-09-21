from __future__ import annotations
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # Stack to keep record of asteroids that survive so far
        
        for ast in asteroids:
            # A new asteroid only collides if it's moving left (negative)
            # and the top of the stack is moving right (positive)
            while stack and ast < 0 and stack[-1] > 0:
                # Compare sizes: absolute value because sizes are magnitudes
                if abs(ast) > stack[-1]:
                    # Current asteroid is bigger, pop the stack (right-moving explodes)
                    stack.pop()
                    # Continue the while to compare with next asteroid in stack
                    # After popping, we need to keep checking collisions
                    continue
                elif abs(ast) == stack[-1]:
                    # Equal sizes -> both explode
                    stack.pop()
                    break  # Break out of while, no need to push current
                else:
                    # Stack top is bigger, current asteroid explodes
                    break
            else:
                # The asteroid survives: push it (either it's moving right, or
                # all asteroids in stack are moving left or stack is empty)
                stack.append(ast)
                
        return stack