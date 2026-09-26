from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        """
        Return a list of all self-dividing numbers in the inclusive range [left, right].
        A self-dividing number is divisible by every digit it contains and has no zero digits.
        """
        result = []
        for num in range(left, right + 1):
            if self._is_self_dividing(num):
                result.append(num)
        return result

    def _is_self_dividing(self, num: int) -> bool:
        """Check if num is self-dividing: contains no zero and divisible by each digit."""
        original = num
        while num > 0:
            digit = num % 10          # extract last digit
            # zero digit or not divisible by this digit -> invalid
            if digit == 0 or original % digit != 0:
                return False
            num //= 10                # remove last digit
        return True                   # all digits passed