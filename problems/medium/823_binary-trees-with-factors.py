class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        
        # Sort the array so we can process roots in increasing order
        arr_sorted = sorted(arr)
        # Set for O(1) lookup of whether a factor is present
        values = set(arr_sorted)
        # dp[x] = number of binary trees with root value x
        dp = {}
        
        # Process each value as a potential root
        for root_val in arr_sorted:
            # A single node (leaf) tree is always valid
            total = 1
            
            # Try all possible left child values (b) that are less than root_val
            # Since both children must be >1 and product = root_val,
            # the left child must be a factor of root_val and less than root_val.
            for left_val in arr_sorted:
                if left_val >= root_val:
                    break  # Because arr_sorted is sorted ascending
                if root_val % left_val != 0:
                    continue  # Not a factor
                right_val = root_val // left_val
                if right_val in values:
                    # left_val and right_val are both valid children.
                    # The number of trees for this pair is dp[left_val] * dp[right_val].
                    # Since left and right children are distinct positions,
                    # even if left_val == right_val, the product is correct.
                    total = (total + dp[left_val] * dp[right_val]) % MOD
            
            dp[root_val] = total
        
        # Sum over all root values for the final answer
        result = sum(dp.values()) % MOD
        return result