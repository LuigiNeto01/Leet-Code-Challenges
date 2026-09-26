from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # Step 1: Build counter for letters in licensePlate (case-insensitive, ignore non-letters)
        license_counter = Counter()
        for ch in licensePlate:
            if ch.isalpha():               # Only letters matter
                license_counter[ch.lower()] += 1

        # Step 2: Scan words, find the shortest completing word
        best_word = None
        best_len = float('inf')

        for word in words:
            # Optimization: skip words longer than current best
            if len(word) >= best_len:
                continue

            # Build counter for the current word (already lowercase)
            word_counter = Counter(word)

            # Check if word has at least the required count for each letter
            is_completing = True
            for letter, required_count in license_counter.items():
                if word_counter.get(letter, 0) < required_count:
                    is_completing = False
                    break

            if is_completing:
                # Found a valid word, and it's shorter (since we skipped longer ones)
                best_word = word
                best_len = len(word)

        # Problem guarantees an answer exists, so best_word is not None
        return best_word