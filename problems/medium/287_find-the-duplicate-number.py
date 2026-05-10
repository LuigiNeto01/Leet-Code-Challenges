from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Cycle Detection (Tortoise and Hare)
        # Treat array as a linked list where nums[i] points to index nums[i]
        # Since there's a duplicate, there must be a cycle
        
        # Phase 1: Find intersection point in the cycle
        # slow moves 1 step, fast moves 2 steps
        slow = nums[0]
        fast = nums[0]
        
        # Move until they meet inside the cycle
        while True:
            slow = nums[slow]  # move 1 step
            fast = nums[nums[fast]]  # move 2 steps
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle (the duplicate number)
        # Start one pointer from beginning, keep other at intersection
        # Move both at same speed - they'll meet at cycle entrance
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        # The meeting point is the duplicate number
        return slow