class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        # Count frequency of each digit in secret and guess (excluding bulls)
        secret_counts = [0] * 10  # for digits 0-9
        guess_counts = [0] * 10
        
        # First pass: count bulls and collect non-bull digits
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                # Exact match at same position = bull
                bulls += 1
            else:
                # Track non-bull digits for cow counting
                secret_counts[int(secret[i])] += 1
                guess_counts[int(guess[i])] += 1
        
        # Second pass: count cows from non-bull digits
        # Cows are digits that exist in both but at wrong positions
        for digit in range(10):
            # Take minimum count - if secret has 2 '1's and guess has 3 '1's (all non-bull),
            # only 2 can be cows since we can only match what exists in secret
            cows += min(secret_counts[digit], guess_counts[digit])
        
        return f"{bulls}A{cows}B"