class Solution:
    def climbStairs(self, n: int) -> int:
        # Each step you can take 1 or 2 steps. Number of ways follows Fibonacci:
        # ways(1)=1, ways(2)=2, ways(n)=ways(n-1)+ways(n-2) for n>=3.
        # Use iterative constant-space DP to compute the nth value.
        if n <= 0:
            # problem constraints say n >= 1, but handle non-positive defensively
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        # prev corresponds to ways(i-2), curr to ways(i-1) initially for i=3
        prev, curr = 1, 2
        # iterate from step 3 up to n computing ways incrementally
        for _ in range(3, n + 1):
            # next number is sum of previous two (Fibonacci relation)
            prev, curr = curr, prev + curr
            # prev becomes old curr, curr becomes new ways(i)
        return curr