from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        tx, ty = target

        # Minimum turns needed for the player to reach the target.
        player_dist = abs(tx) + abs(ty)

        for gx, gy in ghosts:
            # If any ghost can reach the target no later than the player,
            # it can wait there and catch the player on arrival.
            ghost_dist = abs(gx - tx) + abs(gy - ty)
            if ghost_dist <= player_dist:
                return False

        return True