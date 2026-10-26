from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr: list[int]) -> str:
        best_total = -1          # total minutes of best time found so far
        best_str = ""            # string representation of best time

        # Try every permutation of the 4 digits
        for h1, h2, m1, m2 in permutations(arr):
            hours = h1 * 10 + h2
            minutes = m1 * 10 + m2

            # Check if this forms a valid 24-hour time
            if 0 <= hours < 24 and 0 <= minutes < 60:
                total = hours * 60 + minutes
                # Keep the latest time (largest total minutes)
                if total > best_total:
                    best_total = total
                    best_str = f"{hours:02d}:{minutes:02d}"

        # If no valid time was found, best_total stays -1 -> return empty string
        return best_str