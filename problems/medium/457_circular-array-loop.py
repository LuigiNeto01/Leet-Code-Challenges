from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def get_next(idx):
            return (idx + nums[idx]) % n
        
        for i in range(n):
            if nums[i] == 0:
                continue
            
            slow = fast = i
            direction = nums[i] > 0
            
            while True:
                # Move slow pointer one step
                prev_slow = slow
                slow = get_next(slow)
                
                # Check validity of slow
                if nums[slow] == 0 or (nums[slow] > 0) != direction:
                    break
                # Check for self-loop
                if slow == get_next(slow):
                    break
                
                # Move fast pointer first step
                prev_fast = fast
                fast = get_next(fast)
                
                # Check validity of fast after first step
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break
                # Check for self-loop
                if fast == get_next(fast):
                    break
                
                # Move fast pointer second step
                fast = get_next(fast)
                
                # Check validity of fast after second step
                if nums[fast] == 0 or (nums[fast] > 0) != direction:
                    break
                # Check for self-loop
                if fast == get_next(fast):
                    break
                
                # Check if slow meets fast
                if slow == fast:
                    return True
            
            # Mark all nodes in this path as invalid
            slow = i
            direction = nums[i] > 0
            while (nums[slow] > 0) == direction and nums[slow] != 0:
                next_idx = get_next(slow)
                if next_idx == slow:
                    nums[slow] = 0
                    break
                nums[slow] = 0
                slow = next_idx
        
        return False