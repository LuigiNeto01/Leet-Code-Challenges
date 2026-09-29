class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # dp[i] = ways to decode first i characters (prefix length i)
        # We only need last two values to compute next.
        prev2 = 1  # dp[0] = 1 (empty string)
        prev1 = 1  # dp[1] will be computed from s[0] alone
        # Actually we start loop for i=1..len(s), with prev1 representing dp[i-1] before update.
        # We'll set prev1 to 1 initially which corresponds to dp[0] when i=1.
        # But careful: we need to handle single-char decoding first.
        # We'll iterate i from 1 to n:
        #   prev1 = dp[i-1] (ways up to i-1)
        #   prev2 = dp[i-2] (ways up to i-2)
        
        n = len(s)
        for i in range(1, n + 1):
            cur = 0
            ch = s[i-1]
            # 1) decode single character
            if ch == '0':
                ways_single = 0
            elif ch == '*':
                ways_single = 9  # digits 1..9
            else:  # '1'..'9'
                ways_single = 1
            cur = (cur + prev1 * ways_single) % MOD
            
            # 2) decode two characters (i-2 and i-1)
            if i >= 2:
                first = s[i-2]
                second = s[i-1]
                ways_two = 0
                # Both digits
                if first.isdigit() and second.isdigit():
                    val = int(first) * 10 + int(second)
                    if 10 <= val <= 26:
                        ways_two = 1
                elif first == '*' and second == '*':
                    # Both wildcard: valid pairs: (1,1..9) = 9, (2,1..6) = 6 => total 15
                    ways_two = 15
                elif first.isdigit() and second == '*':
                    # first digit, second wildcard
                    if first == '1':
                        ways_two = 9  # 11..19
                    elif first == '2':
                        ways_two = 6  # 21..26
                    else:
                        ways_two = 0
                elif first == '*' and second.isdigit():
                    # first wildcard, second digit
                    if second == '0':
                        # only "10" or "20"
                        ways_two = 2
                    elif '1' <= second <= '6':
                        # first can be 1 or 2
                        ways_two = 2
                    else:  # '7'..'9'
                        # only first=1 works
                        ways_two = 1
                # else invalid -> ways_two = 0
                cur = (cur + prev2 * ways_two) % MOD
            
            # shift for next iteration
            prev2 = prev1
            prev1 = cur
        
        # prev1 now holds dp[n]
        return prev1 % MOD