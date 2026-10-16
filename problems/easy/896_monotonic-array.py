class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        # Single pass: track whether the array can be increasing or decreasing
        increasing = True
        decreasing = True
        
        # Compare each adjacent pair
        for i in range(1, len(nums)):
            # If current element is greater than previous, not decreasing
            if nums[i] > nums[i-1]:
                decreasing = False
            # If current element is less than previous, not increasing
            elif nums[i] < nums[i-1]:
                increasing = False
            
            # Early exit: if both flags are False, array is not monotonic
            if not increasing and not decreasing:
                return False
        
        # If we never eliminated both possibilities, it's monotonic
        return increasing or decreasing