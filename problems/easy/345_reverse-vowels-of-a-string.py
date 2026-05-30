class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define vowels set for O(1) lookup (both lower and upper case)
        vowels = set('aeiouAEIOU')
        
        # Convert string to list for in-place swapping (strings are immutable)
        chars = list(s)
        
        # Two pointers: one from start, one from end
        left = 0
        right = len(chars) - 1
        
        while left < right:
            # Move left pointer until we find a vowel
            while left < right and chars[left] not in vowels:
                left += 1
            
            # Move right pointer until we find a vowel
            while left < right and chars[right] not in vowels:
                right -= 1
            
            # Swap the vowels at left and right pointers
            chars[left], chars[right] = chars[right], chars[left]
            
            # Move both pointers inward
            left += 1
            right -= 1
        
        # Convert list back to string
        return ''.join(chars)