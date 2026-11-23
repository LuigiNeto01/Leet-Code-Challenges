from __future__ import annotations

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        # Count how many primes are in [1, n]
        # Use Sieve of Eratosthenes to determine primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark multiples of i as non-prime
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        prime_count = sum(is_prime)  # number of primes <= n
        non_prime_count = n - prime_count  # numbers that are not prime

        # Factorial function with modulo
        def factorial_mod(k: int) -> int:
            result = 1
            for i in range(2, k + 1):
                result = (result * i) % MOD
            return result

        # The prime numbers must occupy the prime-indexed positions (1-indexed).
        # Number of ways = (prime_count)! * (non_prime_count)!
        # Because we permute primes among prime indices, and non-primes among the rest.
        ans = (factorial_mod(prime_count) * factorial_mod(non_prime_count)) % MOD
        return ans