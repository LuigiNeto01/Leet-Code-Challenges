from collections import deque

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        """
        Returns all integers of length n where the absolute difference between
        every two consecutive digits is exactly k.
        """
        # BFS/DFS approach: start from digits 1..9 (no leading zero),
        # then repeatedly append next possible digit (last digit +/- k) if valid.
        
        result = []
        
        # Use iterative BFS: queue stores tuples (current_number, remaining_length)
        # current_number is built digit by digit.
        # We start with single-digit numbers (length 1) from 1 to 9.
        queue = deque()
        for first_digit in range(1, 10):
            queue.append((str(first_digit), n - 1))  # remaining digits to append
        
        while queue:
            num_str, remaining = queue.popleft()
            if remaining == 0:
                # Full number formed
                result.append(int(num_str))
            else:
                last_digit = int(num_str[-1])
                # Possible next digits: last_digit - k and last_digit + k
                # Must be in [0..9]
                candidates = set()
                if last_digit - k >= 0:
                    candidates.add(last_digit - k)
                if last_digit + k <= 9:
                    candidates.add(last_digit + k)
                for next_digit in sorted(candidates):  # sorted for deterministic order (optional)
                    new_str = num_str + str(next_digit)
                    queue.append((new_str, remaining - 1))
        
        return result