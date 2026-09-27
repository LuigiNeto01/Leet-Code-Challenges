class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # Get grid dimensions
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        
        # If the new color is the same as the original, no change needed
        if original_color == color:
            return image
        
        # Use DFS with a stack to avoid recursion limits (grid is small, either works)
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            # Process only valid cells that still have the original color
            if 0 <= r < rows and 0 <= c < cols and image[r][c] == original_color:
                # Change to the target color
                image[r][c] = color
                # Add all four neighbors
                stack.append((r + 1, c))
                stack.append((r - 1, c))
                stack.append((r, c + 1))
                stack.append((r, c - 1))
        
        return image