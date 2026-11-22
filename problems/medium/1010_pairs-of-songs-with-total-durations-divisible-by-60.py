from __future__ import annotations

class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        # Use a frequency array for remainders when dividing by 60 (size 60)
        remainder_counts = [0] * 60
        pair_count = 0

        for duration in time:
            # Compute remainder of current song duration mod 60
            rem = duration % 60

            # The complement remainder we need for a valid pair:
            # If rem == 0, we need another song with remainder 0.
            # Otherwise, we need remainder (60 - rem).
            complement = (60 - rem) % 60

            # Add the number of previous songs whose remainder matches complement.
            # This counts all pairs where current song is the second element.
            pair_count += remainder_counts[complement]

            # Update the frequency for the current remainder for future songs.
            remainder_counts[rem] += 1

        return pair_count