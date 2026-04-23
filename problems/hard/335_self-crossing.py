from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        # Iterate through moves and check three crossing cases that can occur.
        # These cases are sufficient to detect any self-crossing in this spiral movement.
        n = len(distance)
        # If fewer than 4 moves, cannot cross itself (need at least 4 for a loop)
        for i in range(n):
            # Case 1: Current line crosses the line 3 steps ahead (simple inward crossing).
            # Happens when current move extends far enough to meet or pass the segment two moves before,
            # while the previous move is not longer than the segment three moves before.
            if i >= 3:
                if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                    return True

            # Case 2: Current line meets the line 4 steps ahead exactly forming a touch (overlap).
            # This is the "edge-touching" case where the previous move equals the move three steps before,
            # and current move plus the move four steps before reaches or passes the move two steps before.
            if i >= 4:
                if distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                    return True

            # Case 3: Complex overlap where the current line crosses the line 5 steps ahead.
            # Several inequalities ensure the shape folds back and overlaps in the interior.
            # This is needed for scenarios not covered by the first two simpler cases.
            if i >= 5:
                # We require the inner segment (i-2) to be longer than (i-4) so folding occurs,
                # and the current move plus distance[i-4] reaches or passes distance[i-2],
                # and the previous move plus distance[i-5] reaches or passes distance[i-3],
                # plus the previous move is not longer than distance[i-3] (to avoid other cases).
                if (distance[i-2] > distance[i-4] and
                    distance[i] + distance[i-4] >= distance[i-2] and
                    distance[i-1] + distance[i-5] >= distance[i-3] and
                    distance[i-1] <= distance[i-3]):
                    return True

        # No crossing detected after checking all moves
        return False