class Solution:
    def divisorGame(self, n: int) -> bool:
        # Key insight: This is a mathematical game problem.
        # If n is even, Alice can always win by choosing x = 1.
        # If n is odd, Alice loses because she can only choose an odd divisor,
        # making n even for Bob, who then can force a win.
        # Base case: n = 1 (odd) -> Alice loses as no valid x exists.
        # Proof by induction: odd numbers have only odd divisors,
        # subtracting an odd from an odd gives an even number.
        # The first player with an even number can always win.
        return n % 2 == 0