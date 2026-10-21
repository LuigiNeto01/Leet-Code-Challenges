from __future__ import annotations

class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10**9 + 7
        # Since arr[i] is between 0 and 100, we can count frequencies.
        freq = [0] * 101
        for x in arr:
            freq[x] += 1

        ans = 0
        # Enumerate possible values a <= b <= c
        for a in range(101):
            if freq[a] == 0:
                continue
            for b in range(a, 101):
                if freq[b] == 0:
                    continue
                # Compute c such that a + b + c == target
                c = target - a - b
                if c < b or c > 100:  # enforce ordering a<=b<=c and valid range
                    continue
                if freq[c] == 0:
                    continue
                fa, fb, fc = freq[a], freq[b], freq[c]

                # All three equal: choose any three indices from the same value
                if a == b == c:
                    # Combination: C(fa, 3)
                    ways = fa * (fa - 1) * (fa - 2) // 6
                elif a == b:  # a == b != c
                    # Choose two from a, one from c
                    ways = (fa * (fa - 1) // 2) * fc
                elif b == c:  # a != b == c
                    # Choose one from a, two from b
                    ways = fa * (fb * (fb - 1) // 2)
                else:  # all distinct
                    ways = fa * fb * fc

                ans = (ans + ways) % MOD

        return ans