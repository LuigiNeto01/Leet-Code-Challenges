class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case: the first term is "1"
        if n == 1:
            return "1"
        
        # Start with the first term
        result = "1"
        
        # Iteratively build up to the nth term
        for i in range(2, n + 1):
            # Build the next term by applying RLE to current result
            next_result = []
            j = 0
            
            # Process current result string character by character
            while j < len(result):
                # Current character to count
                char = result[j]
                count = 1
                
                # Count consecutive occurrences of the same character
                while j + count < len(result) and result[j + count] == char:
                    count += 1
                
                # Append count followed by the character (RLE format)
                next_result.append(str(count))
                next_result.append(char)
                
                # Move to the next different character
                j += count
            
            # Update result for the next iteration
            result = "".join(next_result)
        
        return result