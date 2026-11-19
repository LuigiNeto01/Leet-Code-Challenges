from functools import lru_cache
from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            # Minimum triangulation score for polygon from vertex i to j (clockwise)
            # Base case: if i+1 == j, it's just an edge, no triangle possible
            if j - i < 2:
                return 0
            
            res = float('inf')
            # Choose vertex k between i+1 and j-1 to form triangle (i, k, j)
            for k in range(i + 1, j):
                # Triangle (i,k,j) splits polygon into two subpolygons: (i,k) and (k,j)
                current_score = values[i] * values[k] * values[j]
                total = dp(i, k) + dp(k, j) + current_score
                res = min(res, total)
            return res
        
        return dp(0, n - 1)