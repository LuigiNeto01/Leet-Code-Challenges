from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Dutch National Flag:
        # [0..low-1] are 0s, [low..mid-1] are 1s, [high+1..end] are 2s
        low = 0
        mid = 0
        high = len(nums) - 1

        # Process each unknown element exactly once
        while mid <= high:
            if nums[mid] == 0:
                # Put 0 into the left region and grow both left/processed parts
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 already belongs in the middle region
                mid += 1
            else:
                # Put 2 into the right region
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Do not advance mid here:
                # the swapped-in value is still unclassified