class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Approach: Use bitwise XOR with n shifted right by 1.
        # If n has alternating bits (e.g., 101), then n ^ (n >> 1)
        # will produce a number consisting entirely of 1's (e.g., 111).
        # Then checking if that number + 1 is a power of two validates it.
        
        # Step 1: Create a number where adjacent differing bits produce all 1's.
        # For alternating bits, every adjacent pair differs, so XOR gives 1 for each pair.
        xor_result = n ^ (n >> 1)
        
        # Step 2: Check if xor_result is of the form 111...111 (all bits set).
        # This is true if (xor_result & (xor_result + 1)) == 0 for numbers >= 1.
        # Edge case: xor_result can be 0 if n has only 1 bit (like n=1), 
        # but by constraint n >= 1, and a single bit is trivially alternating.
        # For n=1, xor_result = 0, then (0 & 1) == 0 -> true, correct.
        return (xor_result & (xor_result + 1)) == 0