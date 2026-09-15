class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # A perfect number must be positive and greater than 1 (1 has no proper divisors)
        if num <= 1:
            return False

        total = 1  # 1 is always a divisor for num > 1
        # Check divisors up to sqrt(num)
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                # Add the paired divisor, but avoid double-counting when i == num//i
                if i != num // i:
                    total += num // i
            i += 1

        return total == num