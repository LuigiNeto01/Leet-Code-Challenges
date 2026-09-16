from __future__ import annotations

class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the integer to a list of digits for easy swapping
        digits = list(str(num))
        
        # Keep track of the last occurrence index of each digit (0-9)
        last_pos = {int(d): i for i, d in enumerate(digits)}
        
        # Scan from left to right; for each digit, try to find a larger digit to its right
        for i, d in enumerate(digits):
            current_digit = int(d)
            # Check digits from 9 down to current+1, because we want the largest possible swap
            for larger in range(9, current_digit, -1):
                if larger in last_pos and last_pos[larger] > i:
                    # Swap the current digit with the rightmost occurrence of the larger digit
                    j = last_pos[larger]
                    digits[i], digits[j] = digits[j], digits[i]
                    # Once a swap is made, return immediately (maximum possible achieved)
                    return int(''.join(digits))
        
        # If no swap improves the number, return original
        return num