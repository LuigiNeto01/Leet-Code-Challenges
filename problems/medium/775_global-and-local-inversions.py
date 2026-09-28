class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        """
        For a permutation, every local inversion is also a global inversion.
        So the number of global inversions equals the number of local inversions
        if and only if there are NO "non-local" global inversions — i.e., 
        no pair (i, j) with j > i+1 and nums[i] > nums[j].
        
        This condition is equivalent to: for every i, |nums[i] - i| <= 1.
        Because if a number is more than 1 position away from its correct index,
        it must create a non-local inversion with something in between.
        
        Proof: Since the array is a permutation of [0..n-1], if any element
        is at index i but its value differs from i by more than 1, then there
        exists some element it skipped over, forming a non-local inversion.
        """
        # Check the necessary and sufficient condition
        for i, val in enumerate(nums):
            if abs(val - i) > 1:
                return False
        return True