from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadane's algorithm for maximum subarray sum (non-circular)
        # and minimum subarray sum, plus total sum.
        # The maximum circular sum is either the linear maximum,
        # or total sum - minimum subarray sum (which represents a wrap-around subarray).
        # If all numbers are negative, the answer is the linear maximum.

        total = 0
        # current running maximum/minimum
        max_ending = 0
        min_ending = 0
        # overall maximum/minimum
        max_sofar = -float('inf')
        min_sofar = float('inf')

        for x in nums:
            total += x

            # update max subarray sum ending here (Kadane)
            max_ending = max(x, max_ending + x)
            max_sofar = max(max_sofar, max_ending)

            # update min subarray sum ending here (Kadane for min)
            min_ending = min(x, min_ending + x)
            min_sofar = min(min_sofar, min_ending)

        # if all elements are negative, max_sofar is the answer
        if max_sofar < 0:
            return max_sofar

        # otherwise, take the better of the linear max and the circular max
        return max(max_sofar, total - min_sofar)