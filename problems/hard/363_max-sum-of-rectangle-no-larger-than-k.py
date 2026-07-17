from typing import List
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        
        # Iterate over all pairs of columns (left, right)
        # For smaller dimension, iterate over that to optimize
        for left in range(n):
            # row_sums[i] will store sum of elements from column left to right in row i
            row_sums = [0] * m
            
            for right in range(left, n):
                # Update row_sums to include current column
                for i in range(m):
                    row_sums[i] += matrix[i][right]
                
                # Now we have a 1D array problem: find max subarray sum <= k
                # Use prefix sums with sorted set to find the best subarray
                
                # We want: prefix[j] - prefix[i] <= k
                # Which means: prefix[i] >= prefix[j] - k
                # For each prefix[j], find smallest prefix[i] >= prefix[j] - k
                
                prefix_sums = [0]  # Sorted list of prefix sums seen so far
                current_sum = 0
                
                for row_sum in row_sums:
                    current_sum += row_sum
                    
                    # Find the smallest prefix_sum >= current_sum - k
                    target = current_sum - k
                    idx = bisect_left(prefix_sums, target)
                    
                    # Check if we found a valid prefix sum
                    if idx < len(prefix_sums):
                        candidate = current_sum - prefix_sums[idx]
                        max_sum = max(max_sum, candidate)
                    
                    # Insert current_sum into sorted list
                    insort(prefix_sums, current_sum)
        
        return max_sum