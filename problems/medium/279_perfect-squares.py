class Solution:
    def numSquares(self, n: int) -> int:
        # Dynamic programming approach
        # dp[i] = minimum number of perfect squares that sum to i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 requires 0 perfect squares
        
        # Precompute all perfect squares up to n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        # For each number from 1 to n
        for i in range(1, n + 1):
            # Try subtracting each perfect square
            for square in squares:
                if square > i:
                    break  # No point checking larger squares
                # Update dp[i] by considering using this square
                # dp[i - square] is the min count to reach (i - square)
                # Adding 1 more square to that gives us i
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]