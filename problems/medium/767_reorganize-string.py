from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Count frequency of each character
        freq = Counter(s)
        # Build a max heap based on frequency (use negative for max)
        # Each element: (-frequency, character)
        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)
        
        result = []
        # Variable to hold the previous character and its remaining count
        prev_char = None
        prev_count = 0
        
        while heap:
            # Get the character with the highest remaining frequency
            neg_cnt, ch = heapq.heappop(heap)
            cnt = -neg_cnt
            
            # Append this character to result
            result.append(ch)
            
            # The previous character can now be re-added to heap if still has count
            if prev_count > 0:
                heapq.heappush(heap, (-prev_count, prev_char))
            
            # Update previous with current character, decreasing its count
            prev_char = ch
            prev_count = cnt - 1
        
        # Check if we used all characters with no adjacency violation
        if len(result) != len(s):
            return ""  # Not possible to rearrange
        return ''.join(result)