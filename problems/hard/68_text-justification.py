from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        
        while i < len(words):
            # Greedily pack as many words as possible into current line
            line_words = [words[i]]
            line_length = len(words[i])
            i += 1
            
            # Keep adding words while they fit (with at least 1 space between)
            while i < len(words) and line_length + 1 + len(words[i]) <= maxWidth:
                line_words.append(words[i])
                line_length += 1 + len(words[i])  # +1 for the space
                i += 1
            
            # Check if this is the last line
            is_last_line = (i == len(words))
            
            # Format the line based on whether it's the last line or not
            if is_last_line or len(line_words) == 1:
                # Left-justified: join words with single space, pad right
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                # Fully justified: distribute spaces evenly
                total_chars = sum(len(word) for word in line_words)
                total_spaces = maxWidth - total_chars
                gaps = len(line_words) - 1  # Number of gaps between words
                
                # Calculate spaces per gap and extra spaces for leftmost gaps
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                
                line = ''
                for j, word in enumerate(line_words):
                    line += word
                    if j < gaps:  # Not the last word
                        # Add base spaces plus one extra if this is a leftmost gap
                        line += ' ' * (spaces_per_gap + (1 if j < extra_spaces else 0))
            
            result.append(line)
        
        return result