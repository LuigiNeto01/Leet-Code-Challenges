from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        # Initialize result matrix with same dimensions
        result = [[0] * n for _ in range(m)]
        
        # Directions for 3x3 neighborhood (9 cells including center)
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),  (0, 0),  (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                # Sum over all 9 possible neighbors, but only valid ones
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n:
                        total += img[ni][nj]
                        count += 1
                # Integer division (floor) -- same as math.floor(total / count)
                result[i][j] = total // count
        
        return result