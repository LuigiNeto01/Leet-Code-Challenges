# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Binary search between 1 and n (inclusive) to locate the picked number.
        # Using inclusive bounds simplifies reasoning about loop termination.
        low = 1
        high = n

        # Loop invariant: the picked number is always within [low, high].
        while low <= high:
            # Compute mid safely to avoid potential overflow in other languages.
            mid = low + (high - low) // 2

            # Ask the provided API whether mid is high/low/correct.
            res = guess(mid)

            if res == 0:
                # Found the picked number exactly.
                return mid
            elif res < 0:
                # mid is higher than the picked number -> reduce upper bound.
                # We can safely discard mid itself.
                high = mid - 1
            else:
                # res > 0: mid is lower than the picked number -> increase lower bound.
                # Discard mid itself and search above.
                low = mid + 1

        # According to the problem constraints there is always a valid pick in [1, n].
        # This return is a fallback; in practice loop should always return earlier.
        return -1