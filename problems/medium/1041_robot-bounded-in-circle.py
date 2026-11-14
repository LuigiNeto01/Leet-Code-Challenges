class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Direction vectors: 0=North (0,1), 1=East (1,0), 2=South (0,-1), 3=West (-1,0)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0          # starting position
        d = 0              # starting direction index (North)

        for ch in instructions:
            if ch == 'G':
                dx, dy = dirs[d]
                x += dx
                y += dy
            elif ch == 'L':
                d = (d - 1) % 4   # turn left:  anti-clockwise (d+3 also works)
            else:  # ch == 'R'
                d = (d + 1) % 4   # turn right: clockwise

        # If we are back at origin OR not facing north, the robot is bounded.
        # Reason: if direction changed, the net displacement over 4 cycles cancels out.
        return (x == 0 and y == 0) or d != 0