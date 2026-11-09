from __future__ import annotations  # Allow forward references for type hints
import bisect  # For binary search on times list

class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        """
        Precompute the leading candidate at each vote time.
        Store (time, leader) pairs for binary search queries.
        """
        n = len(persons)
        # Track vote counts per person
        vote_count = {}
        # Current leader (most recent in case of tie)
        current_leader = -1
        # Max votes seen so far (to detect ties)
        max_votes = 0
        
        # Precompute leader after each time point
        self.leaders = []  # list of (time, leader)
        
        for i in range(n):
            person = persons[i]
            time = times[i]
            
            # Increment vote count for this person
            vote_count[person] = vote_count.get(person, 0) + 1
            current_votes = vote_count[person]
            
            # Check if this person becomes the new leader
            # Tie goes to the most recent vote (i.e., the current person if they tie)
            if current_votes > max_votes:
                max_votes = current_votes
                current_leader = person
            elif current_votes == max_votes:
                # Tie: the most recent vote wins, so this person becomes leader
                current_leader = person
                # max_votes stays the same
            
            # Store the leader at this time
            self.leaders.append((time, current_leader))
        
        # Keep times separate for binary search
        self.times = times

    def q(self, t: int) -> int:
        """
        Return the leader at or before time t.
        Use binary search on times to find the rightmost time <= t.
        """
        # Find the largest index where times[idx] <= t
        # bisect_right returns insertion point after any existing entries
        idx = bisect.bisect_right(self.times, t) - 1
        # idx will be -1 only if t < times[0], but constraints say t >= times[0]
        return self.leaders[idx][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)