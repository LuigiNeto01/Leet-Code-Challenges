class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Sort nums1 to easily access smallest and largest remaining elements
        nums1_sorted = sorted(nums1)
        n = len(nums1)
        # Pair each nums2 value with its original index, sort by value descending
        indexed_nums2 = sorted([(nums2[i], i) for i in range(n)], reverse=True)
        # Prepare result array
        res = [0] * n
        # Pointers: left (smallest), right (largest) in sorted nums1
        left, right = 0, n - 1
        # Process nums2 from largest to smallest
        for val, idx in indexed_nums2:
            # If the largest remaining nums1 can beat this nums2, assign it
            if nums1_sorted[right] > val:
                res[idx] = nums1_sorted[right]
                right -= 1
            else:
                # Otherwise, sacrifice the smallest remaining value
                res[idx] = nums1_sorted[left]
                left += 1
        return res