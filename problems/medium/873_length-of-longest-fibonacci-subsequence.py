class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        n = len(arr)
        # Map each value to its index for O(1) lookups
        value_to_index = {val: i for i, val in enumerate(arr)}

        # dp[j][k] = length of longest Fibonacci-like subsequence ending with arr[j], arr[k]
        # Initially every pair forms a length‑2 subsequence
        dp = [[2] * n for _ in range(n)]

        max_len = 0

        # k is the index of the last element of the subsequence
        for k in range(n):
            # j is the index of the second-to-last element
            for j in range(k):
                # We need arr[i] + arr[j] == arr[k]  =>  arr[i] = arr[k] - arr[j]
                target = arr[k] - arr[j]
                # Because arr is strictly increasing, target < arr[j] implies its index i < j.
                # Also the target must exist.
                if target < arr[j] and target in value_to_index:
                    i = value_to_index[target]
                    # Extend the subsequence [..., arr[i], arr[j]] by arr[k]
                    dp[j][k] = dp[i][j] + 1
                    if dp[j][k] > max_len:
                        max_len = dp[j][k]

        # Need at least length 3 to be a valid Fibonacci-like subsequence
        return max_len if max_len >= 3 else 0