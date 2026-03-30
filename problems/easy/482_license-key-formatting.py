class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Remove existing dashes and normalize letters once.
        cleaned = []
        for ch in s:
            if ch != '-':
                cleaned.append(ch.upper())
        
        # If nothing remains, the formatted key is empty.
        if not cleaned:
            return ""
        
        # Build groups from the end so every later group has exactly k chars.
        parts = []
        i = len(cleaned)
        while i > 0:
            start = max(0, i - k)
            # Join this chunk and store it; reversing later restores order.
            parts.append(''.join(cleaned[start:i]))
            i = start
        
        # Parts were collected right-to-left, so reverse before joining.
        return '-'.join(reversed(parts))