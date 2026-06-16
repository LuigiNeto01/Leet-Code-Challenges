from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # Key insight: The optimal target is the median of the array
        # The median minimizes the sum of absolute deviations
        # Proof: For any point, moving left/right from median increases total distance
        
        # Sort the array to find the median
        nums.sort()
        
        # Find the median element
        # For odd length: middle element
        # For even length: either of the two middle elements works (we use lower middle)
        median = nums[len(nums) // 2]
        
        # Calculate total moves: sum of absolute differences from median
        moves = 0
        for num in nums:
            moves += abs(num - median)
        
        return moves