class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (target + 1)
        for face in range(1, min(k, target) + 1):
            dp[face] = 1
        
        for dice in range(2, n + 1):
            new_dp = [0] * (target + 1)
            min_sum = dice
            max_sum = min(target, dice * k)
            for current_sum in range(min_sum, max_sum + 1):
                for face in range(1, k + 1):
                    prev_sum = current_sum - face
                    if prev_sum < dice - 1 or prev_sum > (dice - 1) * k:
                        continue
                    if prev_sum >= 0:
                        new_dp[current_sum] = (new_dp[current_sum] + dp[prev_sum]) % MOD
            dp = new_dp
        
        return dp[target] if n > 0 else 0