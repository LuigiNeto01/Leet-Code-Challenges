class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Store obstacle positions for O(1) lookup.
        obstacle_set = {(x, y) for x, y in obstacles}

        # Directions in order: north, east, south, west.
        # +1 direction index turns right, -1 turns left.
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x = y = 0
        d = 0
        ans = 0

        for cmd in commands:
            if cmd == -2:      # Turn left 90 degrees
                d = (d - 1) % 4
            elif cmd == -1:    # Turn right 90 degrees
                d = (d + 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    # Stop before an obstacle; do not move into it.
                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)

        return ans