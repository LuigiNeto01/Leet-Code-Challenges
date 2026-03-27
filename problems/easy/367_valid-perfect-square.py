class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary search over possible integer roots.
        # If some mid satisfies mid * mid == num, num is a perfect square.
        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            # Found the exact square root.
            if square == num:
                return True

            # Mid is too small, so the root must be larger.
            if square < num:
                left = mid + 1
            else:
                # Mid is too large, so the root must be smaller.
                right = mid - 1

        # No integer root exists.
        return False