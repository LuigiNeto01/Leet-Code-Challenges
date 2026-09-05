class Solution:
    def countArrangement(self, n: int) -> int:
        # Backtracking with bitmask for used numbers
        # n <= 15, so recursion depth is small

        def dfs(pos: int, used: int) -> int:
            # pos: current position (1-indexed) to fill
            if pos > n:
                # all positions filled successfully
                return 1
            total = 0
            # try each number from 1 to n
            for num in range(1, n + 1):
                # check if num is already used
                if (used >> (num - 1)) & 1:
                    continue
                # condition: either num divisible by pos or pos divisible by num
                if num % pos == 0 or pos % num == 0:
                    # mark num as used, recurse to next position
                    total += dfs(pos + 1, used | (1 << (num - 1)))
            return total

        # start recursion at position 1, no numbers used yet
        return dfs(1, 0)