from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        # Count frequencies of each number
        freq = Counter(arr)

        # Process numbers in increasing order of absolute value.
        # This ensures that when we pair x with 2*x, we don't later
        # need to use that 2*x for a different partner.
        for x in sorted(freq, key=abs):
            # If x has already been used (count zero after subtracting), skip
            if freq[x] == 0:
                continue

            # For x to pair, we need exactly freq[x] copies of 2*x
            needed = freq[x]
            # Check if enough 2*x are available
            if freq[2 * x] < needed:
                return False

            # Use up the pairs: remove the used copies of x and 2*x
            freq[2 * x] -= needed
            # x's count becomes zero (it won't be processed again)
            # (Not strictly necessary but good for clarity)
            freq[x] = 0

        return True