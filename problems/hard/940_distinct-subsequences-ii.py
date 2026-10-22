from __future__ import annotations

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # dp array stores the count of distinct subsequences ending with each character 'a'..'z'
        # We only need 26 entries for lowercase letters
        dp = [0] * 26
        
        for ch in s:
            index = ord(ch) - ord('a')
            # Total distinct subsequences so far (including empty) 
            # is sum of all dp + 1 (empty subsequence)
            total = (sum(dp) + 1) % MOD
            
            # The new subsequences ending with ch are: 
            #   all existing subsequences (including empty) + ch
            # But we must subtract the previously counted subsequences that end with the same ch
            # to avoid double counting (they are already included in dp[index])
            new_count = (total - dp[index]) % MOD
            
            # Update dp for current character
            dp[index] = (dp[index] + new_count) % MOD
        
        # The answer is sum of all distinct non-empty subsequences
        # which is total distinct minus the empty subsequence
        result = (sum(dp) % MOD)
        return result