from __future__ import annotations

class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        # Sort people by weight to enable efficient pairing
        people.sort()
        # Two-pointer technique: lightest at left, heaviest at right
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:
            # If the lightest and heaviest can share a boat, pair them
            if people[left] + people[right] <= limit:
                left += 1   # lightest is taken
            # Heaviest always goes on a boat (either alone or paired)
            right -= 1
            boats += 1

        return boats