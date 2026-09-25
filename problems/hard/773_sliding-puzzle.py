from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Flatten board into a tuple for hashing
        start = tuple(num for row in board for num in row)
        target = (1, 2, 3, 4, 5, 0)

        # Legal moves for the empty tile (0) in the flattened board
        neighbors = {
            0: (1, 3),
            1: (0, 2, 4),
            2: (1, 5),
            3: (0, 4),
            4: (1, 3, 5),
            5: (2, 4),
        }

        # BFS queue stores: state, position of 0, number of moves
        q = deque([(start, start.index(0), 0)])
        seen = {start}

        while q:
            state, pos0, dist = q.popleft()

            if state == target:
                return dist

            # Convert tuple to list to perform swaps
            cur = list(state)

            for nxt in neighbors[pos0]:
                # Swap 0 with an adjacent tile
                cur[pos0], cur[nxt] = cur[nxt], cur[pos0]
                new_state = tuple(cur)

                if new_state not in seen:
                    seen.add(new_state)
                    q.append((new_state, nxt, dist + 1))

                # Swap back to try other moves from this state
                cur[pos0], cur[nxt] = cur[nxt], cur[pos0]

        # If BFS exhausts all reachable states, puzzle is unsolvable
        return -1