class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # Convert input strings to integers for comparison
        L = int(left)
        R = int(right)
        
        count = 0
        
        # Generate all palindromic numbers up to sqrt(10^18) = 10^9.
        # Maximum length of such a root is 9 digits (since 10^9 has 10 digits, but 10^9 is not a palindrome? Actually 10^9 is 1,000,000,000 not palindrome. But we need roots up to sqrt(R) <= 10^9, so lengths 1..9.
        for length in range(1, 10):
            half_len = (length + 1) // 2            # number of digits in the first half
            start = 10 ** (half_len - 1) if half_len > 1 else 1   # smallest half of this length (no leading zeros)
            end = 10 ** half_len - 1                # largest half of this length
            
            for half in range(start, end + 1):
                s = str(half)
                # Build palindrome of given length
                if length % 2 == 0:
                    pal_str = s + s[::-1]           # even length: mirror fully
                else:
                    pal_str = s + s[-2::-1]         # odd length: mirror without last digit
                
                root = int(pal_str)                 # this is a palindrome candidate for the root
                sq = root * root
                
                # Since roots are generated in increasing order within this length,
                # if square exceeds R we can stop for this length.
                if sq > R:
                    break
                
                if sq >= L:
                    sq_str = str(sq)
                    if sq_str == sq_str[::-1]:      # check if square is palindrome
                        count += 1
        
        return count