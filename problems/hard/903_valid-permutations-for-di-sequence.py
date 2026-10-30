class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)                     # length of the pattern, permutation length = n+1
        
        # ------------- precompute binomial coefficients C[n][k] modulo MOD ----------
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD
        
        # dp[l][r] : number of valid permutations for substring s[l:r] (right exclusive)
        # l and r are indices in [0, n]. Base: empty substring -> 1 permutation.
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][i] = 1
        
        # DP over increasing substring length
        for length in range(1, n + 1):                    # length of pattern = number of conditions
            for l in range(0, n - length + 1):
                r = l + length
                total = 0
                # p = number of elements placed to the left of the maximum (which is 'length')
                for p in range(0, length + 1):
                    # left condition: left neighbor of max must be 'I' (if it exists)
                    if p > 0 and s[l + p - 1] != 'I':
                        continue
                    # right condition: right neighbor of max must be 'D' (if it exists)
                    if p < length and s[l + p] != 'D':
                        continue
                    
                    # recursively count left and right parts
                    left_ways = dp[l][l + p - 1] if p > 0 else 1
                    right_ways = dp[l + p + 1][r] if p < length else 1
                    
                    # choose which p of the 'length' smaller numbers go to the left side
                    ways = comb[length][p] * left_ways % MOD * right_ways % MOD
                    total = (total + ways) % MOD
                    
                dp[l][r] = total
        
        # the whole string s[0:n] gives the answer
        return dp[0][n]