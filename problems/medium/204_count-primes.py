class Solution:
    def countPrimes(self, n: int) -> int:
        # Edge case: numbers less than 2 have no primes
        if n <= 2:
            return 0
        
        # Sieve of Eratosthenes algorithm
        # Initialize all numbers as potentially prime (True)
        is_prime = [True] * n
        
        # 0 and 1 are not prime
        is_prime[0] = is_prime[1] = False
        
        # Start from 2, the first prime number
        # Only need to check up to sqrt(n) because any composite number
        # less than n must have a factor <= sqrt(n)
        i = 2
        while i * i < n:
            # If i is still marked as prime
            if is_prime[i]:
                # Mark all multiples of i as not prime
                # Start from i*i because smaller multiples already marked
                # by smaller primes
                for j in range(i * i, n, i):
                    is_prime[j] = False
            i += 1
        
        # Count how many True values remain (these are primes)
        return sum(is_prime)