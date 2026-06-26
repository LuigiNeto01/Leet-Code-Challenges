# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Binary search to find the first bad version
        # Since all versions after a bad version are also bad,
        # we're looking for the leftmost bad version
        
        left = 1  # Start from version 1
        right = n  # End at version n
        
        while left < right:
            # Calculate mid to avoid overflow (though Python handles big ints well)
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # If mid is bad, the first bad version is at mid or before
                # So search in the left half (including mid)
                right = mid
            else:
                # If mid is good, the first bad version must be after mid
                # So search in the right half (excluding mid)
                left = mid + 1
        
        # When left == right, we've found the first bad version
        return left