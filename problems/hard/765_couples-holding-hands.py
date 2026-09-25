from __future__ import annotations

class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        # Map each person to their current seat index
        pos = [0] * len(row)
        for i, person in enumerate(row):
            pos[person] = i

        swaps = 0
        # Process each pair of adjacent seats (0-1, 2-3, ...)
        for i in range(0, len(row), 2):
            # Person at first seat of the pair
            p1 = row[i]
            # The expected partner (if p1 is even then partner = p1+1, else p1-1)
            partner = p1 ^ 1  # XOR with 1 flips the least significant bit: even->+1, odd->-1

            # Person currently sitting at the second seat of the pair
            p2 = row[i + 1]
            # If they are not already a couple, need a swap
            if p2 != partner:
                # Find where the partner currently is (its index)
                partner_idx = pos[partner]
                # Swap the person at the second seat (p2) with the partner
                row[i + 1], row[partner_idx] = row[partner_idx], row[i + 1]
                # Update position mapping for the swapped people
                pos[p2] = partner_idx
                pos[partner] = i + 1
                swaps += 1

        return swaps