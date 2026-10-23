class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        # Two-pointer approach: place evens at front, odds at back.
        left = 0
        right = len(nums) - 1
        
        while left < right:
            # Move left forward if it's already even.
            if nums[left] % 2 == 0:
                left += 1
            # Move right backward if it's already odd.
            elif nums[right] % 2 == 1:
                right -= 1
            # Otherwise swap odd (at left) with even (at right).
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        return nums