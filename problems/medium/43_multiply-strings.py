class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle edge case: if either number is "0", product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # Result can have at most m + n digits
        result = [0] * (m + n)
        
        # Reverse iterate through both numbers (right to left, like manual multiplication)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply current digits
                mul = int(num1[i]) * int(num2[j])
                # Position in result array (counting from right)
                p1 = i + j      # position for carry
                p2 = i + j + 1  # position for current digit
                
                # Add multiplication result to existing value at p2
                mul += result[p2]
                
                # Store the ones digit at p2
                result[p2] = mul % 10
                # Add carry to p1
                result[p1] += mul // 10
        
        # Convert result array to string, skipping leading zeros
        result_str = ''.join(map(str, result))
        # Remove leading zeros (but keep at least one digit)
        return result_str.lstrip('0') or '0'