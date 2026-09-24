class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        # Track number of modifications used
        modified = False

        for i in range(len(nums) - 1):
            # Found a violation: nums[i] > nums[i+1]
            if nums[i] > nums[i+1]:
                # If already modified once before, impossible
                if modified:
                    return False

                # Decide which element to adjust to fix the violation
                # Option A: lower nums[i] to nums[i+1] – check if it keeps non-decreasing left side
                if i == 0 or nums[i-1] <= nums[i+1]:
                    # Lower nums[i] to match nums[i+1] (modify the larger one)
                    nums[i] = nums[i+1]
                else:
                    # Option B: raise nums[i+1] to nums[i] (modify the smaller one)
                    nums[i+1] = nums[i]

                modified = True

        # At most one modification needed
        return True