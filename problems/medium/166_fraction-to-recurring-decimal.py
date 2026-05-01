class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle zero numerator case
        if numerator == 0:
            return "0"
        
        result = []
        
        # Handle sign: negative if exactly one of numerator/denominator is negative
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        
        # Work with absolute values to simplify division logic
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
        
        # If no remainder, return integer part
        if remainder == 0:
            return "".join(result)
        
        # Add decimal point for fractional part
        result.append(".")
        
        # Track remainders and their positions to detect cycles
        # Key: remainder, Value: position in result where this remainder first appeared
        remainder_map = {}
        
        # Process fractional part
        while remainder != 0:
            # If we've seen this remainder before, we have a repeating cycle
            if remainder in remainder_map:
                # Insert opening parenthesis at the start of the cycle
                cycle_start = remainder_map[remainder]
                result.insert(cycle_start, "(")
                result.append(")")
                break
            
            # Record position of current remainder (before appending next digit)
            remainder_map[remainder] = len(result)
            
            # Perform long division step
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
        
        return "".join(result)