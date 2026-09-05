class Solution:
    def findIntegers(self, n: int) -> int:
        # Get binary representation of n (without '0b')
        s = bin(n)[2:]
        L = len(s)

        # dp[i] = number of valid binary strings of exact length i (no consecutive ones)
        # Recurrence: dp[i] = dp[i-1] + dp[i-2], base dp[0]=1, dp[1]=2.
        dp = [0] * (L + 2)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, L + 2):
            dp[i] = dp[i-1] + dp[i-2]

        # Count all numbers with fewer bits than n (including 0)
        # For length i (i>=1), number of valid i-bit numbers = dp[i-1] ?? Not exactly.
        # We derived: for i=1 -> 1 (number 1); for i>=2 -> dp[i-2].
        ans = 1  # the number 0 is always valid
        for i in range(1, L):
            if i == 1:
                ans += 1          # single bit: only the number 1
            else:
                ans += dp[i - 2]  # numbers with exactly i bits (MSB=1)

        # Now process bits of n itself (same length) from most significant to least.
        # Start with the first bit (MSB), which is always 1 for n>=1.
        prev_bit = 1  # the first bit is 1
        # Process the remaining bits (positions 1 .. L-1)
        for i in range(1, L):
            bit = int(s[i])
            remaining = L - i - 1   # number of bits after this position
            if bit == 1:
                # Option: set this bit to 0 -> all valid suffixes of length 'remaining' are allowed
                ans += dp[remaining]
                # If previous bit is also 1, we cannot keep this 1 (consecutive ones)
                if prev_bit == 1:
                    # Prefix already invalid; n itself cannot be valid, so stop here
                    return ans
                # Otherwise, we keep this 1 and continue
                prev_bit = 1
            else:
                # bit is 0, just update previous bit
                prev_bit = 0

        # If we processed all bits without breaking, n itself is valid
        ans += 1
        return ans