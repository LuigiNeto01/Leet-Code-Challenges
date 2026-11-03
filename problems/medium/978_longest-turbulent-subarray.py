class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n

        best = 1          # A single element is always turbulent.
        current = 1       # Length of current turbulent subarray ending at i.
        prev_sign = 0     # Comparison sign between arr[i-2] and arr[i-1].

        for i in range(1, n):
            # Compute comparison sign: 1 for rising, -1 for falling, 0 for equal.
            if arr[i] > arr[i - 1]:
                sign = 1
            elif arr[i] < arr[i - 1]:
                sign = -1
            else:
                sign = 0

            if sign == 0:
                # Equal neighbors break turbulence; only this element remains valid.
                current = 1
            elif prev_sign == 0 or sign == prev_sign:
                # First comparison or same direction means a new length-2 subarray.
                current = 2
            else:
                # Alternating direction extends the current turbulent subarray.
                current += 1

            best = max(best, current)
            prev_sign = sign

        return best