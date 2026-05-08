class Solution:
    def toHex(self, num: int) -> str:
        # Special case: zero
        if num == 0:
            return "0"
        
        # For negative numbers, convert to 32-bit two's complement representation
        # In Python, we can use bitwise AND with 0xFFFFFFFF to get 32-bit unsigned value
        if num < 0:
            num = num & 0xFFFFFFFF
        
        # Hex digit mapping
        hex_chars = "0123456789abcdef"
        result = []
        
        # Extract hex digits from right to left
        while num > 0:
            # Get the last 4 bits (one hex digit)
            digit = num & 0xF
            result.append(hex_chars[digit])
            # Shift right by 4 bits
            num >>= 4
        
        # Reverse since we built from right to left
        return ''.join(reversed(result))