class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        """
        Sorts array such that even indices have even numbers and odd indices have odd numbers.
        Uses two-pointer approach for O(n) time and O(1) extra space (in-place).
        """
        # Initialize two pointers:
        # even_ptr will look for misplaced even positions (0-indexed: 0, 2, 4, ...)
        # odd_ptr will look for misplaced odd positions (1-indexed: 1, 3, 5, ...)
        even_ptr = 0
        odd_ptr = 1
        n = len(nums)
        
        # Continue until we've checked all positions
        while even_ptr < n and odd_ptr < n:
            # If current even position already has an even number, move to next even position
            if nums[even_ptr] % 2 == 0:
                even_ptr += 2
            # If current odd position already has an odd number, move to next odd position
            elif nums[odd_ptr] % 2 == 1:
                odd_ptr += 2
            # Otherwise, both positions have wrong parity, swap them
            else:
                # nums[even_ptr] is odd and nums[odd_ptr] is even, swap to fix both
                nums[even_ptr], nums[odd_ptr] = nums[odd_ptr], nums[even_ptr]
                # After swap, both positions are now correct, advance both pointers
                even_ptr += 2
                odd_ptr += 2
        
        return nums