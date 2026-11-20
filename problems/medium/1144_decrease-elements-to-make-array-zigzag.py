class Solution:
    def movesToMakeZigzag(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        moves1 = 0  # Pattern 1: even indices are peaks
        moves2 = 0  # Pattern 2: odd indices are peaks
        
        # Pattern 1: even indices are peaks, odd are valleys
        temp = nums.copy()
        for i in range(1, n, 2):  # odd indices (valleys) need to be less than neighbors
            left = temp[i-1]
            right = temp[i+1] if i+1 < n else float('inf')
            target = min(left, right)
            if temp[i] >= target:
                diff = temp[i] - (target - 1)
                moves1 += diff
                temp[i] -= diff
        
        # Pattern 2: odd indices are peaks, even are valleys
        temp = nums.copy()
        for i in range(0, n, 2):  # even indices (valleys) need to be less than neighbors
            left = temp[i-1] if i > 0 else float('inf')
            right = temp[i+1] if i+1 < n else float('inf')
            target = min(left, right)
            if temp[i] >= target:
                diff = temp[i] - (target - 1)
                moves2 += diff
                temp[i] -= diff
        
        return min(moves1, moves2)