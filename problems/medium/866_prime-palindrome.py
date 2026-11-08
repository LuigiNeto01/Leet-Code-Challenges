from __future__ import annotations

class Solution:
    def primePalindrome(self, n: int) -> int:
        # Handle small n explicitly for speed.
        if n <= 2:
            return 2

        # Primality test with trial division.
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True

        # Generate all palindromes of a given length in increasing order.
        def generate_palindromes(length: int):
            # Single-digit palindromes: 1..9
            if length == 1:
                for d in range(1, 10):
                    yield d
                return

            # Even length: only length 2 is possible prime (11 is prime)
            if length % 2 == 0:
                if length == 2:
                    for prefix in range(1, 10):
                        yield int(str(prefix) + str(prefix)[::-1])
                # All even-length palindromes longer than 2 are divisible by 11 -> skip.
                return

            # Odd length: take first half (including middle digit) and mirror without last digit.
            half = (length + 1) // 2
            start = 10 ** (half - 1)
            end = 10 ** half - 1
            for prefix in range(start, end + 1):
                s = str(prefix)
                yield int(s + s[-2::-1])

        # Start from the length of n, go up to length 9 (since answer <= 2*10^8).
        start_len = len(str(n))
        for length in range(start_len, 10):  # lengths 1..9 inclusive
            # Skip even lengths > 2 — they are never prime.
            if length % 2 == 0 and length > 2:
                continue
            for p in generate_palindromes(length):
                if p >= n and is_prime(p):
                    return p

        # The problem guarantees an answer, but this line serves as a safety net.
        return -1