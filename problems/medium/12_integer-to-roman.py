class Solution:
    def intToRoman(self, num: int) -> str:
        # Define value-symbol pairs in descending order
        # Include subtractive forms (4, 9, 40, 90, 400, 900)
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        result = []
        
        # Greedily subtract the largest possible value
        for i in range(len(values)):
            # How many times does this value fit into num?
            count = num // values[i]
            if count:
                # Append the symbol that many times
                result.append(symbols[i] * count)
                # Reduce num by the amount we've converted
                num -= values[i] * count
        
        return ''.join(result)