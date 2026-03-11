class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindromes because of the leading '-'.
        if x < 0:
            return False
        
        # Any number ending in 0 cannot be a palindrome unless the number is 0 itself,
        # because reversed form would need a leading 0, which integers do not keep.
        if x != 0 and x % 10 == 0:
            return False
        
        reversed_half = 0
        
        # Reverse only the last half of the digits.
        # This avoids overflow concerns and keeps the logic simple.
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10
        
        # For even digit counts: x should equal reversed_half.
        # For odd digit counts: middle digit does not matter, so drop it with // 10.
        return x == reversed_half or x == reversed_half // 10