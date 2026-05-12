class Solution:
    def frequencySort(self, s: str) -> str:
        # Count frequency of each character
        from collections import Counter
        freq = Counter(s)
        
        # Sort characters by frequency in descending order
        # Counter.most_common() returns list of (char, count) tuples sorted by count
        sorted_chars = freq.most_common()
        
        # Build result by repeating each character by its frequency
        result = []
        for char, count in sorted_chars:
            result.append(char * count)
        
        return ''.join(result)