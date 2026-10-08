class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Precompute all primes up to 20 (max set bits for numbers <= 10^6 is 20)
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        count = 0
        # Iterate over the inclusive range
        for num in range(left, right + 1):
            # Count set bits using bin() and .count()
            bits = bin(num).count('1')
            if bits in primes:
                count += 1
        return count