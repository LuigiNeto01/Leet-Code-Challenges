class Solution:
    def convertToBase7(self, num: int) -> str:
        # Handle zero separately to avoid loop issues.
        if num == 0:
            return "0"
        
        # Remember sign, then work with absolute value.
        sign = '-' if num < 0 else ''
        n = abs(num)
        
        digits = []
        # Repeatedly divide by 7 and collect remainders.
        while n > 0:
            digits.append(str(n % 7))
            n //= 7
        
        # Remainders are in reverse order; prepend sign if needed.
        return sign + ''.join(reversed(digits))