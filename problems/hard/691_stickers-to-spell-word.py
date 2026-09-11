from functools import lru_cache
from typing import List

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Preprocess stickers into character frequency counters (26 letters)
        # This avoids scanning full sticker strings repeatedly
        sticker_counts = []
        for s in stickers:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - 97] += 1
            sticker_counts.append(cnt)
        
        # Pre-filter: if any character in target does not appear in any sticker, impossible
        target_set = set(target)
        for ch in target_set:
            found = False
            for cnt in sticker_counts:
                if cnt[ord(ch) - 97] > 0:
                    found = True
                    break
            if not found:
                return -1
        
        n = len(target)
        
        @lru_cache(None)
        def dfs(mask: int) -> int:
            # mask: bitmask representing which positions of target are already covered
            # Returns minimum stickers needed to cover remaining characters
            if mask == (1 << n) - 1:
                return 0  # all characters covered
            
            # Find first uncovered character index (greedy heuristic to reduce branching)
            first_uncovered = 0
            while mask & (1 << first_uncovered):
                first_uncovered += 1
            
            answer = float('inf')
            
            # Try each sticker
            for cnt in sticker_counts:
                # Only consider sticker that contains the first uncovered char
                # This is an optimization: if sticker can't help with current char, skip
                if cnt[ord(target[first_uncovered]) - 97] == 0:
                    continue
                
                # Apply this sticker: update mask with newly covered positions
                new_mask = mask
                # Make a working copy of sticker counts to avoid modifying original
                sticker_available = cnt[:]
                
                # Try to cover as many uncovered positions as possible
                for j in range(n):
                    if not (new_mask & (1 << j)):
                        idx = ord(target[j]) - 97
                        if sticker_available[idx] > 0:
                            sticker_available[idx] -= 1
                            new_mask |= (1 << j)
                
                # Only recurse if we actually covered something new
                if new_mask != mask:
                    answer = min(answer, 1 + dfs(new_mask))
            
            return answer
        
        result = dfs(0)
        return result if result != float('inf') else -1