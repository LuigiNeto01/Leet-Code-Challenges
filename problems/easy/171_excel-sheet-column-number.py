class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # This is a base-26 number system where A=1, B=2, ..., Z=26
        # Similar to converting from any base to decimal
        # For example: "AB" = A*26^1 + B*26^0 = 1*26 + 2 = 28
        
        result = 0
        
        # Process each character from left to right
        for char in columnTitle:
            # Convert character to its numeric value (A=1, B=2, etc.)
            digit = ord(char) - ord('A') + 1
            
            # Shift previous result by multiplying by 26 (the base)
            # and add the current digit
            result = result * 26 + digit
        
        return result