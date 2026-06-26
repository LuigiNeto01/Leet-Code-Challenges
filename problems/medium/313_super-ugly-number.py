from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Dynamic programming approach: generate ugly numbers in sorted order
        # ugly[i] will store the (i+1)-th super ugly number
        ugly = [0] * n
        ugly[0] = 1  # First super ugly number is always 1
        
        # For each prime, maintain a pointer indicating which ugly number to multiply next
        # pointers[i] tracks the index in ugly[] for primes[i]
        pointers = [0] * len(primes)
        
        # Generate n super ugly numbers
        for i in range(1, n):
            # Calculate candidates: each prime multiplied by the ugly number at its pointer
            candidates = [primes[j] * ugly[pointers[j]] for j in range(len(primes))]
            
            # The next ugly number is the minimum of all candidates
            next_ugly = min(candidates)
            ugly[i] = next_ugly
            
            # Advance pointers for all primes that produced this minimum
            # (handles duplicates: if multiple primes generate same value, advance all)
            for j in range(len(primes)):
                if candidates[j] == next_ugly:
                    pointers[j] += 1
        
        # Return the nth super ugly number
        return ugly[n - 1]