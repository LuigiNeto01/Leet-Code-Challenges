from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Queues store the indices of senators from each party.
        # The index indicates their position in the initial order.
        radiant = deque()
        dire = deque()
        n = len(senate)

        # Populate queues with the initial positions.
        for i, party in enumerate(senate):
            if party == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simulate the voting rounds.
        # Each round: the senator with the smaller index bans the other.
        # The winning senator gets a new index (current + n) to be placed
        # after all current senators, preserving the cyclic order.
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            if r_idx < d_idx:
                # Radiant bans a Dire, Radiant survives to next round.
                radiant.append(r_idx + n)
            else:
                # Dire bans a Radiant, Dire survives.
                dire.append(d_idx + n)

        # The party with remaining senators wins.
        return "Radiant" if radiant else "Dire"