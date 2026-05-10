class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Count frequency of each character in magazine
        from collections import Counter
        
        # Create frequency maps for both strings
        magazine_count = Counter(magazine)
        ransom_count = Counter(ransomNote)
        
        # Check if magazine has enough of each character needed for ransomNote
        for char, count in ransom_count.items():
            # If character not in magazine or not enough occurrences
            if magazine_count[char] < count:
                return False
        
        return True