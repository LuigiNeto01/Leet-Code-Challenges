from __future__ import annotations
import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # We'll accumulate the result as a fraction: num / den
        total_num = 0
        total_den = 1
        
        i = 0
        n = len(expression)
        
        while i < n:
            # Determine the sign of the current fraction: +1 or -1
            sign = 1
            if expression[i] == '+':
                sign = 1
                i += 1
            elif expression[i] == '-':
                sign = -1
                i += 1
            # else: first fraction has no sign, default positive
            
            # Extract numerator: digits until '/'
            num_start = i
            while i < n and expression[i] != '/':
                i += 1
            numerator = int(expression[num_start:i])
            
            # Skip '/'
            i += 1  # after '/'
            
            # Extract denominator: digits until next sign or end
            den_start = i
            while i < n and expression[i] not in ('+', '-'):
                i += 1
            denominator = int(expression[den_start:i])
            
            # Apply sign to numerator
            numerator *= sign
            
            # Add current fraction to total: total_num/total_den + numerator/denominator
            # common denominator = total_den * denominator
            total_num = total_num * denominator + numerator * total_den
            total_den *= denominator
            
            # Reduce fraction by GCD to keep numbers small and end with irreducible
            g = math.gcd(abs(total_num), total_den)
            total_num //= g
            total_den //= g
        
        # If result is an integer, denominator should be 1
        # (already reduced, so if denominator is 1 it's fine)
        return f"{total_num}/{total_den}"