from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # If empty (not in constraints), player1 cannot lose; treat as win
        if not nums:
            return True

        n = len(nums)
        # dp[i][j] will store the maximum score difference the current player can achieve
        # over the other player from the subarray nums[i..j] assuming both play optimally.
        # A positive value means current player leads by that amount.
        dp = [[0] * n for _ in range(n)]

        # Base case: when i == j, only one number available, current player takes it.
        for i in range(n):
            dp[i][i] = nums[i]

        # Fill DP for increasing lengths (from 2 to n)
        # We iterate i from n-1 down to 0 so that dp[i+1][j] is already computed.
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # If current player picks nums[i], their net advantage is nums[i] - (best opponent advantage on remaining)
                pick_left = nums[i] - dp[i + 1][j]
                # If current player picks nums[j], net advantage is nums[j] - dp[i][j-1]
                pick_right = nums[j] - dp[i][j - 1]
                # Current player will choose the option that maximizes their net advantage
                dp[i][j] = max(pick_left, pick_right)

        # If the max difference for the whole array is >= 0, player 1 can win or tie (tie counts as win)
        return dp[0][n - 1] >= 0