class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # Number of ways to write n as sum of consecutive positive integers.
        # We iterate over possible number of terms k.
        # For a given k, the sum is: k * a + k*(k-1)//2 = n
        # where a is the first term (positive integer).
        # Rearranged: a = (n - k*(k-1)//2) / k.
        # a must be integer >= 1, so (n - k*(k-1)//2) % k == 0 and quotient >= 1.
        # k can go up to when k*(k+1)//2 <= n (since smallest sum for k terms is 1+2+...+k).
        count = 0
        k = 1
        # Stop when the minimum sum of k positive integers exceeds n
        while k * (k + 1) // 2 <= n:
            # t = sum of first (k-1) integers, i.e., k*(k-1)//2
            t = k * (k - 1) // 2
            remainder = (n - t) % k
            if remainder == 0:
                a = (n - t) // k
                if a >= 1:
                    count += 1
            k += 1
        return count