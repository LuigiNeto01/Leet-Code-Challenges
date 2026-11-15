from __future__ import annotations

class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        n = len(tops)
        # Since numbers are only 1..6, we can try each possible target value
        INF = 10 ** 9
        best = INF

        for target in range(1, 7):
            # Check if we can make all tops equal to target
            tops_possible = True
            rotations_tops = 0  # number of dominoes to rotate to achieve tops = target
            # Check if we can make all bottoms equal to target
            bottoms_possible = True
            rotations_bottoms = 0  # number of dominoes to rotate to achieve bottoms = target

            for i in range(n):
                top = tops[i]
                bottom = bottoms[i]

                # For making tops all target:
                # If top already target, no rotation needed
                # If top != target, we must rotate but only if bottom == target
                if top != target:
                    if bottom == target:
                        rotations_tops += 1
                    else:
                        tops_possible = False

                # For making bottoms all target:
                if bottom != target:
                    if top == target:
                        rotations_bottoms += 1
                    else:
                        bottoms_possible = False

            if tops_possible:
                best = min(best, rotations_tops)
            if bottoms_possible:
                best = min(best, rotations_bottoms)

        return -1 if best == INF else best