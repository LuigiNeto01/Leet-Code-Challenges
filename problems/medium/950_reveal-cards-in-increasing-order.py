from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        n = len(deck)
        deck.sort()

        # result[pos] will hold the card that should be placed at that index
        result = [0] * n

        # Simulate the reveal order using indices, not actual cards yet
        indices = deque(range(n))

        # Assign the smallest remaining card to the next revealed position
        for card in deck:
            idx = indices.popleft()
            result[idx] = card

            # If cards remain, move the next top index to the bottom
            if indices:
                indices.append(indices.popleft())

        return result