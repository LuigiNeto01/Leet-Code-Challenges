class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Dynamic programming approach: generate ugly numbers in order
        # Each ugly number is derived from previous ugly numbers multiplied by 2, 3, or 5
        
        # Array to store the first n ugly numbers
        ugly = [0] * n
        ugly[0] = 1  # First ugly number is 1
        
        # Three pointers to track which ugly number to multiply next
        # i2, i3, i5 point to indices in ugly array
        i2 = i3 = i5 = 0
        
        # Next multiples of 2, 3, and 5
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5
        
        # Generate ugly numbers from index 1 to n-1
        for i in range(1, n):
            # The next ugly number is the minimum of the three candidates
            next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            ugly[i] = next_ugly
            
            # Advance pointer(s) whose multiple was chosen
            # Use separate ifs (not elif) to handle duplicates
            # e.g., 6 = 2*3 = 3*2, both pointers should advance
            if next_ugly == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly[i2] * 2
            
            if next_ugly == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly[i3] * 3
            
            if next_ugly == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly[i5] * 5
        
        # Return the nth ugly number (at index n-1)
        return ugly[n - 1]