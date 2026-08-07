#!/usr/bin/env python3
import sys

def transpose_file():
    # Read all lines from stdin
    lines = []
    for line in sys.stdin:
        # Strip newline and split by space
        lines.append(line.rstrip('\n').split(' '))
    
    # If no input, return
    if not lines:
        return
    
    # Get number of columns (assuming all rows have same length)
    num_cols = len(lines[0])
    
    # Transpose: iterate through columns and gather elements from each row
    for col_idx in range(num_cols):
        row_elements = []
        for row in lines:
            row_elements.append(row[col_idx])
        # Print the transposed row
        print(' '.join(row_elements))

if __name__ == '__main__':
    transpose_file()