class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize pointers to the end of both strings
        i = len(num1) - 1
        j = len(num2) - 1
        
        # Track carry from previous digit addition
        carry = 0
        
        # Build result from right to left
        result = []
        
        # Process both strings from right to left
        while i >= 0 or j >= 0 or carry:
            # Get digit from num1 (0 if index out of bounds)
            digit1 = int(num1[i]) if i >= 0 else 0
            
            # Get digit from num2 (0 if index out of bounds)
            digit2 = int(num2[j]) if j >= 0 else 0
            
            # Add digits and carry
            total = digit1 + digit2 + carry
            
            # Extract the single digit to append (remainder after dividing by 10)
            result.append(str(total % 10))
            
            # Update carry for next iteration (integer division by 10)
            carry = total // 10
            
            # Move pointers left
            i -= 1
            j -= 1
        
        # Result was built in reverse order, so reverse it
        return ''.join(reversed(result))