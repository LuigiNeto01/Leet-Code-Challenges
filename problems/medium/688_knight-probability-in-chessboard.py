from __future__ import annotations

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # All 8 possible knight moves as (dr, dc) offsets
        moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        
        # dp[r][c] = probability to be on cell (r,c) after current number of moves
        # Initially at step 0: probability 1 at starting position, 0 elsewhere
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0
        
        # Simulate each move step by step
        for step in range(k):
            new_dp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    # If no probability to be at (r,c), skip (minor optimization)
                    if dp[r][c] == 0.0:
                        continue
                    prob = dp[r][c]
                    # Try all 8 knight moves from (r,c)
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        # Only stay on board; if off board, we ignore (probability lost)
                        if 0 <= nr < n and 0 <= nc < n:
                            # Each move chosen uniformly among 8, so divide by 8
                            new_dp[nr][nc] += prob / 8.0
            dp = new_dp
        
        # Sum all probabilities after k moves = probability knight stays on board
        total = 0.0
        for r in range(n):
            total += sum(dp[r])
        return total