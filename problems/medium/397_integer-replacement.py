class Solution:
    def integerReplacement(self, n: int) -> int:
        # Edge case: already 1 needs 0 operations
        if n == 1:
            return 0

        steps = 0
        # Work with Python ints (arbitrary precision) so no overflow concerns.
        # Greedy strategy:
        # - If even: always divide by 2 (best move).
        # - If odd: choose +1 or -1 to maximize trailing zeros after the operation,
        #   which allows more divisions by 2 in subsequent steps.
        # Special-case n == 3: decrementing (3->2->1) is better than incrementing (3->4->2->1).
        while n != 1:
            # Even number -> divide by 2
            if n % 2 == 0:
                # Use right shift mentality: dividing by two reduces one bit.
                n //= 2
                steps += 1
            else:
                # For odd numbers, decide between n+1 and n-1.
                # If n == 3, prefer n-1 (3 -> 2 -> 1).
                # Otherwise, look at n mod 4:
                # - If n mod 4 == 1 -> n-1 yields more trailing zeros than n+1.
                # - If n mod 4 == 3 -> n+1 usually yields more trailing zeros.
                # This heuristic minimizes number of subsequent divisions.
                if n == 3 or n & 3 == 1:
                    n -= 1
                    steps += 1
                else:
                    # n & 3 == 3 and n != 3 -> increment
                    n += 1
                    steps += 1
        return steps