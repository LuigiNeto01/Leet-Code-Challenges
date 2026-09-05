class Solution:
    def fib(self, n: int) -> int:
        # Base cases: F(0) = 0, F(1) = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        # Iterative calculation using two variables to track previous two numbers
        prev2, prev1 = 0, 1  # F(0) and F(1)
        for _ in range(2, n + 1):
            current = prev1 + prev2  # F(i) = F(i-1) + F(i-2)
            prev2, prev1 = prev1, current  # Shift for next iteration
        return prev1