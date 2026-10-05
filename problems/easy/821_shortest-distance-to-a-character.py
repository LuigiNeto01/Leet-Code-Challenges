class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        ans = [n] * n  # initialise with large value (max possible distance)

        # Left-to-right pass: compute distance to nearest 'c' on the left
        prev = -n  # sentinel: no 'c' seen yet (distance will be large)
        for i, ch in enumerate(s):
            if ch == c:
                prev = i
                ans[i] = 0
            # only update if we've already seen a 'c' to the left
            if prev != -n:
                ans[i] = min(ans[i], i - prev)

        # Right-to-left pass: compute distance to nearest 'c' on the right
        prev = n + n  # sentinel: no 'c' seen yet from the right
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
                ans[i] = 0
            # update with distance to next 'c' on the right
            if prev != n + n:
                ans[i] = min(ans[i], prev - i)

        return ans