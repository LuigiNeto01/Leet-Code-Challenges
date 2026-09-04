from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # Get dimensions of the original matrix
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0  # handle empty matrix (though constraints say m>=1)
        
        # Reshape is only possible if total number of elements remains the same
        if m * n != r * c:
            return mat          # return original matrix if reshape is impossible
        
        # Flatten the original matrix row-wise into a single list
        flat = []
        for row in mat:
            flat.extend(row)    # extend is efficient for adding all elements of row
        
        # Build the reshaped matrix row by row
        res = []
        for i in range(r):
            # Slice c consecutive elements from the flat list for each new row
            res.append(flat[i * c : (i + 1) * c])
        
        return res