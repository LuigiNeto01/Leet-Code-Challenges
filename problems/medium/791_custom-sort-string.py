from __future__ import annotations
from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Count frequency of each character in s.
        freq = Counter(s)
        
        # Build result: first add characters in the order they appear in 'order'.
        result_parts = []
        for ch in order:
            if ch in freq:
                # Append this character as many times as it appears in s.
                result_parts.append(ch * freq[ch])
                # Remove so we don't add it again later.
                del freq[ch]
        
        # Append any remaining characters (those not in 'order') at the end.
        # Their relative order doesn't matter, so we just append them all.
        for ch, count in freq.items():
            result_parts.append(ch * count)
        
        return ''.join(result_parts)