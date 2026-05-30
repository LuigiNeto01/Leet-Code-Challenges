class Solution:
    def addDigits(self, num: int) -> int:
        # Special case: if num is 0, return 0
        if num == 0:
            return 0
        
        # Mathematical approach using digital root formula
        # The digital root of a positive integer is obtained by iteratively summing digits
        # until a single digit is obtained.
        # 
        # Key insight: The digital root follows a pattern based on modulo 9:
        # - For any positive integer n, digital_root(n) = 1 + ((n - 1) % 9)
        # 
        # This works because:
        # - A number and the sum of its digits are congruent modulo 9
        # - The digital root cycles through 1,2,3,4,5,6,7,8,9,1,2,... as n increases
        # - When n % 9 == 0 (and n > 0), the digital root is 9, not 0
        # - Formula handles this: 1 + ((n - 1) % 9) gives 9 when n % 9 == 0
        
        return 1 + (num - 1) % 9