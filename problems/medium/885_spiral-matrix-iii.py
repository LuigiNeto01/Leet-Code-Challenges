class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        # Total cells to visit
        total = rows * cols
        result = []
        
        # Starting position
        r, c = rStart, cStart
        
        # Direction order: east, south, west, north
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        
        # Step length increases after every two direction changes
        step_len = 1
        steps_used_in_current_turn = 0
        
        # Continue until we have collected all positions
        while len(result) < total:
            # For the current direction, move step_len steps
            for _ in range(step_len):
                # If within bounds, record the position
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
                # Move in current direction
                dr, dc = dirs[dir_idx]
                r += dr
                c += dc
                
            # Finished moving in current direction, turn clockwise
            dir_idx = (dir_idx + 1) % 4
            steps_used_in_current_turn += 1
            
            # After two direction changes (east→south, then west→north), increase step length
            if steps_used_in_current_turn % 2 == 0:
                step_len += 1
        
        return result