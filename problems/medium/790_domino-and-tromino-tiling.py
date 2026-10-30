class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        # Mask bit 0 = top row, bit 1 = bottom row.
        # trans[in_mask][out_mask] = ways to finish the current column while
        # leaving out_mask cells occupied in the next column.
        trans = [
            [1, 1, 1, 1],  # both empty: vertical, two tromino orientations, two horizontals
            [0, 0, 1, 1],  # top filled: bottom horizontal, or one tromino
            [0, 1, 0, 1],  # bottom filled: top horizontal, or one tromino
            [1, 0, 0, 0],  # both filled: no new tile starts here
        ]

        # No overhang before the first column.
        dp = [1, 0, 0, 0]

        for _ in range(n):
            ndp = [0, 0, 0, 0]
            for in_mask in range(4):
                for out_mask in range(4):
                    ndp[out_mask] = (
                        ndp[out_mask] + dp[in_mask] * trans[in_mask][out_mask]
                    ) % MOD
            dp = ndp

        # A complete tiling cannot extend past the right edge.
        return dp[0]