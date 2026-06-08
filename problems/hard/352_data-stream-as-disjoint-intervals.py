class SummaryRanges:

    def __init__(self):
        # Store intervals as a list of [start, end]
        self.intervals = []
        # Track seen numbers to avoid duplicates
        self.seen = set()

    def addNum(self, value: int) -> None:
        # Skip if already added
        if value in self.seen:
            return
        self.seen.add(value)
        
        # Binary search to find insertion position
        left, right = 0, len(self.intervals)
        while left < right:
            mid = (left + right) // 2
            if self.intervals[mid][0] < value:
                left = mid + 1
            else:
                right = mid
        
        # pos is where value would fit based on start values
        pos = left
        
        # Check if we can merge with previous interval
        merge_prev = pos > 0 and self.intervals[pos - 1][1] >= value - 1
        # Check if we can merge with next interval
        merge_next = pos < len(self.intervals) and self.intervals[pos][0] <= value + 1
        
        if merge_prev and merge_next:
            # Merge with both: extend prev to cover next, remove next
            self.intervals[pos - 1][1] = max(self.intervals[pos - 1][1], self.intervals[pos][1])
            self.intervals.pop(pos)
        elif merge_prev:
            # Merge with previous interval only
            self.intervals[pos - 1][1] = max(self.intervals[pos - 1][1], value)
        elif merge_next:
            # Merge with next interval only
            self.intervals[pos][0] = min(self.intervals[pos][0], value)
        else:
            # Create new interval
            self.intervals.insert(pos, [value, value])

    def getIntervals(self) -> list[list[int]]:
        # Return a copy of intervals
        return self.intervals[:]