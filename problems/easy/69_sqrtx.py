class Solution:
    def mySqrt(self, x: int) -> int:
        # Edge case: sqrt(0) = 0, sqrt(1) = 1
        if x < 2:
            return x
        
        # Binary search for the integer square root
        # Search space: [1, x] but we can optimize to [1, x//2] since sqrt(x) <= x/2 for x >= 4
        left, right = 1, x // 2
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            # Check if mid is the exact or closest (rounded down) square root
            if square == x:
                return mid
            elif square < x:
                # mid might be the answer, but check if there's a larger valid value
                # Store mid as potential answer and search right half
                left = mid + 1
            else:
                # square > x, so mid is too large, search left half
                right = mid - 1
        
        # When loop exits, right is the largest integer where right^2 <= x
        return right