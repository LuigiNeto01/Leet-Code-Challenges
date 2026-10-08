from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # If total cards not divisible by groupSize, impossible
        if len(hand) % groupSize != 0:
            return False

        # Count frequency of each card value
        freq = Counter(hand)

        # Sort unique card values to process in ascending order
        unique_vals = sorted(freq)

        for val in unique_vals:
            # If current card still has remaining count, it must start a new group
            while freq[val] > 0:
                # Try to form a consecutive group of size groupSize starting at val
                for offset in range(groupSize):
                    need = val + offset
                    # If needed card is missing, fail
                    if freq[need] == 0:
                        return False
                    # Use one card of this value
                    freq[need] -= 1

        # All cards successfully grouped
        return True