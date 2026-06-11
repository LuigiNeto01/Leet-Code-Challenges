class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Memoization cache to avoid recomputing same subproblems
        memo = {}
        
        def helper(str1, str2):
            # Base case: if strings are identical, they're scrambled versions
            if str1 == str2:
                return True
            
            # Check if result is already cached
            key = (str1, str2)
            if key in memo:
                return memo[key]
            
            # If character frequencies don't match, can't be scrambled
            if sorted(str1) != sorted(str2):
                memo[key] = False
                return False
            
            n = len(str1)
            
            # Try all possible split points
            for i in range(1, n):
                # Case 1: No swap - left matches left, right matches right
                # str1[:i] should scramble to str2[:i]
                # str1[i:] should scramble to str2[i:]
                if helper(str1[:i], str2[:i]) and helper(str1[i:], str2[i:]):
                    memo[key] = True
                    return True
                
                # Case 2: Swap - left matches right, right matches left
                # str1[:i] should scramble to str2[n-i:] (right part of str2)
                # str1[i:] should scramble to str2[:n-i] (left part of str2)
                if helper(str1[:i], str2[n-i:]) and helper(str1[i:], str2[:n-i]):
                    memo[key] = True
                    return True
            
            # No valid split found
            memo[key] = False
            return False
        
        return helper(s1, s2)