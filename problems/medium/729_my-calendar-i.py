class MyCalendar:

    def __init__(self):
        # Store booked intervals as a list of (start, end) pairs
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Check if the new interval overlaps with any existing booking
        for existing_start, existing_end in self.bookings:
            # Two intervals [s1, e1) and [s2, e2) overlap if:
            # s1 < e2 AND s2 < e1 (half-open interval intersection)
            if startTime < existing_end and existing_start < endTime:
                return False  # Overlap detected, cannot book
        
        # No overlap, add the new interval to the calendar
        self.bookings.append((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)