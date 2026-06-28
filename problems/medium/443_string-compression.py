from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        # write_pos tracks where we write the next compressed character
        write_pos = 0
        # read_pos tracks where we read the next character to process
        read_pos = 0
        
        while read_pos < len(chars):
            # Current character to compress
            current_char = chars[read_pos]
            # Count consecutive occurrences
            count = 0
            
            # Count all consecutive repeating characters
            while read_pos < len(chars) and chars[read_pos] == current_char:
                read_pos += 1
                count += 1
            
            # Write the character
            chars[write_pos] = current_char
            write_pos += 1
            
            # If count > 1, write the count as individual digits
            if count > 1:
                # Convert count to string to get individual digits
                count_str = str(count)
                for digit in count_str:
                    chars[write_pos] = digit
                    write_pos += 1
        
        # Return the new length of the compressed array
        return write_pos