class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        if n == 1:
            return 10
        
        total = 10
        unique_digits = 9
        available_digits = 9
        
        for i in range(2, min(n + 1, 11)):
            unique_digits *= available_digits
            total += unique_digits
            available_digits -= 1
        
        return total