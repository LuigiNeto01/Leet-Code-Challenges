from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Use the array itself as a hash map by marking visited indices
        # For each number, mark its corresponding index (num-1) as negative
        # Numbers at indices that remain positive are the missing numbers
        
        # First pass: mark presence by negating values at corresponding indices
        for num in nums:
            # Get the index this number corresponds to (num-1 since array is 0-indexed)
            # Use abs() because we may have already negated this value
            index = abs(num) - 1
            # Mark this index as "visited" by making it negative (if not already)
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Second pass: collect indices where values are still positive
        # Those indices+1 are the missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                # i+1 was never seen in the array
                result.append(i + 1)
        
        return result