from __future__ import annotations

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        # Morse code for each lowercase English letter, a-z in order.
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."
        ]

        seen_transformations = set()

        for word in words:
            # Concatenate the Morse code of every letter in this word.
            transformation = "".join(morse[ord(ch) - ord('a')] for ch in word)
            seen_transformations.add(transformation)

        # The number of unique transformations is the set size.
        return len(seen_transformations)