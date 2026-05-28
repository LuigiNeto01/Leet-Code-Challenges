class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Two strings are isomorphic if there's a bijection between their characters
        # We need to maintain two mappings:
        # 1. s[i] -> t[i] (each char in s maps to exactly one char in t)
        # 2. t[i] -> s[i] (each char in t maps to exactly one char in s, ensuring one-to-one)
        
        # Map from s characters to t characters
        s_to_t = {}
        # Map from t characters to s characters (to ensure bijection)
        t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            # Check if char_s already has a mapping
            if char_s in s_to_t:
                # If it maps to a different character in t, not isomorphic
                if s_to_t[char_s] != char_t:
                    return False
            else:
                # Create new mapping
                s_to_t[char_s] = char_t
            
            # Check if char_t already has a reverse mapping
            if char_t in t_to_s:
                # If it maps to a different character in s, not isomorphic
                if t_to_s[char_t] != char_s:
                    return False
            else:
                # Create new reverse mapping
                t_to_s[char_t] = char_s
        
        return True