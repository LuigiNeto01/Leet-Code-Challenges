class Solution:
    def romanToInt(self, s: str) -> int:
        # Map each Roman numeral character to its integer value
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Iterate through each character in the Roman numeral string
        for i in range(n):
            # Get the value of the current character
            current_val = roman_map[s[i]]
            
            # Check if there's a next character and if it has a greater value
            # This indicates a subtraction case (e.g., IV, IX, XL, XC, CD, CM)
            if i + 1 < n and roman_map[s[i + 1]] > current_val:
                # Subtract current value because it's part of a subtraction pair
                total -= current_val
            else:
                # Add current value normally
                total += current_val
        
        return total