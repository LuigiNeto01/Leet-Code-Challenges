class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Key insight: When we AND all numbers in a range, any bit position that
        # changes from 0 to 1 or 1 to 0 within the range will result in 0.
        # Only the common prefix bits (that don't change) will remain as 1.
        
        # Example: [5, 7] = [101, 110, 111]
        # 101 & 110 & 111 = 100
        # The rightmost bits flip within the range, only the common left prefix remains.
        
        # Approach: Find the common prefix by right-shifting both numbers
        # until they become equal. Track how many shifts we did.
        
        shift = 0
        
        # Keep shifting right until left and right are equal
        # This removes all the bits that differ in the range
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        
        # Shift back left to restore the common prefix
        # All the bits we shifted out will be 0 in the result
        return left << shift