from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Edge case: if valueDiff is 0, we need exact duplicates within indexDiff
        if indexDiff < 1:
            return False
        
        # Bucket sort approach: group numbers into buckets of size (valueDiff + 1)
        # If two numbers are in the same bucket, their difference is <= valueDiff
        # We also need to check adjacent buckets
        
        bucket_size = valueDiff + 1  # Size of each bucket
        buckets = {}  # Map bucket_id -> number in that bucket
        
        for i, num in enumerate(nums):
            # Calculate which bucket this number belongs to
            # Use floor division to handle negative numbers correctly
            bucket_id = num // bucket_size
            
            # Check if current bucket already has a number (must be within valueDiff)
            if bucket_id in buckets:
                return True
            
            # Check adjacent buckets (left and right)
            # Numbers in adjacent buckets might be within valueDiff
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            # Add current number to its bucket
            buckets[bucket_id] = num
            
            # Maintain sliding window: remove the element that's now outside indexDiff range
            if i >= indexDiff:
                # Remove the oldest element from buckets
                old_num = nums[i - indexDiff]
                old_bucket_id = old_num // bucket_size
                del buckets[old_bucket_id]
        
        return False