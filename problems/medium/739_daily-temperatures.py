class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        # Stores indices for which a warmer day hasn't been found yet.
        # Temperatures corresponding to stack indices are strictly decreasing from bottom.
        stack = []
        ans = [0] * n

        for i in range(n):
            # While current temperature is warmer than the top of the stack,
            # it is the next warmer day for the popped index.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx  # days waited to get a warmer day
            stack.append(i)

        return ans