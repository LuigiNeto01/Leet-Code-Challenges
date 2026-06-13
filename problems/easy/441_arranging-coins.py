class Solution:
    def arrangeCoins(self, n: int) -> int:
        # We need to find the largest k such that k*(k+1)/2 <= n
        # This is equivalent to solving k^2 + k - 2n <= 0
        # Using the quadratic formula: k = (-1 + sqrt(1 + 8n)) / 2
        # We use binary search for a robust integer solution
        
        left, right = 0, n
        
        while left <= right:
            mid = (left + right) // 2
            # Calculate coins needed for mid complete rows: 1+2+...+mid = mid*(mid+1)/2
            coins_needed = mid * (mid + 1) // 2
            
            if coins_needed == n:
                # Exact match - mid rows use exactly n coins
                return mid
            elif coins_needed < n:
                # We can potentially build more rows
                left = mid + 1
            else:
                # Too many coins needed, try fewer rows
                right = mid - 1
        
        # When loop exits, right is the largest k where k*(k+1)/2 <= n
        return right