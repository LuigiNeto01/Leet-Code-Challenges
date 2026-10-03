from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        # Maximum allowed integer (32-bit signed)
        MAX_INT = 2**31 - 1
        
        n = len(num)
        
        # Helper to check if a substring forms a valid number:
        # no leading zero (unless number itself is "0") and fits in 32-bit.
        def is_valid(start: int, length: int) -> bool:
            if length > 1 and num[start] == '0':
                return False
            # Check overflow: we can compare with string representation of MAX_INT
            # or parse later; but for early exit we can compare length.
            # Since MAX_INT has 10 digits (2147483647), if length > 10 it's too large.
            if length > 10:
                return False
            val = int(num[start:start+length])
            return val <= MAX_INT
        
        # Try all possible lengths for the first number (a)
        for len1 in range(1, n // 2 + 1):  # first number can't be more than half
            if not is_valid(0, len1):
                continue
            a = int(num[:len1])
            
            # Try all possible lengths for the second number (b)
            for len2 in range(1, (n - len1) // 2 + 1):  # second also at most half of remaining
                if not is_valid(len1, len2):
                    continue
                b = int(num[len1:len1+len2])
                
                # Build the Fibonacci-like sequence starting with a, b
                seq = [a, b]
                pos = len1 + len2  # current position in num string
                
                # Keep generating next numbers
                while pos < n:
                    # The next number must be a + b
                    nxt = seq[-1] + seq[-2]
                    # Convert to string to compare with substring
                    nxt_str = str(nxt)
                    nxt_len = len(nxt_str)
                    
                    # Check if we have enough characters and they match
                    if pos + nxt_len > n or num[pos:pos+nxt_len] != nxt_str:
                        break
                    
                    # Also ensure no leading zero issue (already satisfied via string match)
                    seq.append(nxt)
                    pos += nxt_len
                    
                    # Early overflow: if nxt > MAX_INT, break (though already string length check)
                    if nxt > MAX_INT:
                        break
                
                # If we consumed the whole string and have at least 3 numbers, return
                if pos == n and len(seq) >= 3:
                    return seq
        
        # No valid sequence found
        return []