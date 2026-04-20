class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Use the "slots" method: each node consumes one slot.
        # Non-null node generates two new child slots; null '#' generates none.
        # Start with one slot for the root.
        tokens = preorder.split(',')
        slots = 1  # initial available position for root

        for i, tok in enumerate(tokens):
            # consume one slot for the current token
            slots -= 1
            # If at any point we don't have a slot to put this node, serialization is invalid
            if slots < 0:
                return False
            # Non-null nodes (numbers) create two additional child slots
            if tok != '#':
                slots += 2
            # Continue until all tokens processed

        # All slots must be exactly filled for a valid serialization (no extra open positions)
        return slots == 0