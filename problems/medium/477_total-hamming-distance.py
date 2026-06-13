from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # Key insight: For each bit position, count how many numbers have 0 vs 1
        # The contribution to total distance from that bit is: count_0 * count_1
        # This is because each 0 pairs with each 1 to contribute 1 to distance
        
        total_distance = 0
        n = len(nums)
        
        # Check each of the 32 bits (since nums[i] <= 10^9 fits in 32 bits)
        for bit_pos in range(32):
            # Count how many numbers have bit set to 1 at this position
            ones_count = 0
            for num in nums:
                # Check if the bit at bit_pos is set
                if (num >> bit_pos) & 1:
                    ones_count += 1
            
            # Numbers with 0 at this bit position
            zeros_count = n - ones_count
            
            # Each pair of (0, 1) at this position contributes 1 to hamming distance
            total_distance += ones_count * zeros_count
        
        return total_distance