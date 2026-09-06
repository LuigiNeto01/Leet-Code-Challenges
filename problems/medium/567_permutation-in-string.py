class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer than s2, no window can match
        if len(s1) > len(s2):
            return False

        # Frequency arrays for 26 lowercase letters
        target = [0] * 26
        window = [0] * 26

        # Build target frequency from s1
        for ch in s1:
            target[ord(ch) - ord('a')] += 1

        # Initial window of length len(s1)
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        # Check first window
        if target == window:
            return True

        # Slide the window through the rest of s2
        for i in range(len(s1), len(s2)):
            # Add new character on the right
            window[ord(s2[i]) - ord('a')] += 1
            # Remove character that exits the window on the left
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1
            # Compare frequencies after each slide
            if target == window:
                return True

        return False