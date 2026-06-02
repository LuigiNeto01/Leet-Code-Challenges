class Solution:
    def largestPalindrome(self, n: int) -> int:
        # Edge case: for n=1, the largest product is 9*9=81, but largest palindrome product is 9
        if n == 1:
            return 9
        
        # Define the range of n-digit numbers
        upper = 10**n - 1  # e.g., for n=2, upper=99
        lower = 10**(n-1)  # e.g., for n=2, lower=10
        
        # Start from the largest possible palindrome and work downwards
        # The largest n-digit product is upper*upper
        # We construct palindromes by creating the left half and mirroring it
        
        # For n digits, the product can have at most 2n digits
        # We try palindromes starting from the largest possible
        for i in range(upper, lower - 1, -1):
            # Create a palindrome by mirroring i
            # e.g., i=99 -> palindrome=9009
            s = str(i)
            palindrome = int(s + s[::-1])
            
            # Check if this palindrome can be expressed as product of two n-digit numbers
            # We only need to check divisors up to upper (the max n-digit number)
            # Start from upper and go down to sqrt(palindrome) or lower bound
            for j in range(upper, lower - 1, -1):
                # If j*j < palindrome, no valid factor pair exists
                if j * j < palindrome:
                    break
                
                # Check if palindrome is divisible by j
                if palindrome % j == 0:
                    quotient = palindrome // j
                    # Check if quotient is also an n-digit number
                    if lower <= quotient <= upper:
                        # Found valid factorization
                        return palindrome % 1337
        
        # Should not reach here given constraints
        return 0