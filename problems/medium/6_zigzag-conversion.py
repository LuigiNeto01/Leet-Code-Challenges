class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # With one row, or very short strings, the zigzag is identical to the input.
        if numRows == 1 or numRows >= len(s):
            return s

        # Build each row separately, then join at the end.
        rows = [[] for _ in range(numRows)]

        # Start at the top row and move downward first.
        curr_row = 0
        direction = 1  # 1 means moving down, -1 means moving up

        for ch in s:
            # Place current character into its zigzag row.
            rows[curr_row].append(ch)

            # Reverse direction at the top or bottom boundary.
            if curr_row == 0:
                direction = 1
            elif curr_row == numRows - 1:
                direction = -1

            # Move to the next row for the next character.
            curr_row += direction

        # Reading row by row produces the required converted string.
        return "".join("".join(row) for row in rows)