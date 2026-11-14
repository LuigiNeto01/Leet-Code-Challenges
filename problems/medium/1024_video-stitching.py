class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        # Sort clips by start time, and for equal start times by end time descending.
        # This helps us greedily pick the clip that extends the current coverage farthest.
        clips.sort(key=lambda x: (x[0], -x[1]))
        
        # Number of clips used so far
        count = 0
        # Current end position we have covered
        current_end = 0
        # The farthest we can reach from the current starting point
        farthest = 0
        i = 0
        n = len(clips)
        
        # Continue while we haven't covered the entire [0, time]
        while current_end < time:
            # Reset farthest for each new segment we try to cover
            farthest = current_end
            
            # Look at all clips that start at or before current_end
            # (they are sorted, so once they start after current_end, stop)
            while i < n and clips[i][0] <= current_end:
                # Update the farthest reachable end from these clips
                farthest = max(farthest, clips[i][1])
                i += 1
            
            # If we cannot extend coverage any further, it's impossible
            if farthest == current_end:
                return -1
            
            # Greedy: take the clip that reaches farthest
            count += 1
            # Move the current coverage end to the farthest reachable point
            current_end = farthest
        
        return count