class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0

        # Work backwards from target to startValue.
        # Reverse operations are: divide by 2 if even, or add 1.
        while target > startValue:
            if target % 2 == 1:
                # An odd target must have been produced by a decrement,
                # so reverse it with an increment.
                target += 1
            else:
                # For an even target, halving is always at least as good
                # as reversing a decrement first.
                target //= 2
            ops += 1

        # Now target <= startValue, so we only need decrements to go down.
        return ops + (startValue - target)