from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Handle empty input case
        if not digits:
            return []
        
        # Map each digit to its corresponding letters (like phone keypad)
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        # Backtracking function to build combinations
        def backtrack(index, current_combination):
            # Base case: if we've processed all digits, add the combination
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            letters = digit_to_letters[current_digit]
            
            # Try each letter for the current digit
            for letter in letters:
                # Recursively build combinations for remaining digits
                backtrack(index + 1, current_combination + letter)
        
        # Start backtracking from index 0 with empty combination
        backtrack(0, "")
        
        return result