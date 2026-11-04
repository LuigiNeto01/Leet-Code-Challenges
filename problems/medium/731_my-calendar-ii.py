class MyCalendarTwo:
    def __init__(self):
        # list of intervals [start, end) for events that are singly booked
        self.single = []
        # list of intervals where exactly two events overlap (double-booked)
        self.double = []

    def book(self, startTime: int, endTime: int) -> bool:
        # 1) Check if the new event would cause triple booking:
        #    if it overlaps any existing double-booked interval, reject it.
        for d_start, d_end in self.double:
            if max(startTime, d_start) < min(endTime, d_end):
                return False

        # 2) Safe to add the event; update the double-booked intervals:
        #    the overlap with every existing single event becomes a new double interval.
        for s_start, s_end in self.single:
            overlap_start = max(startTime, s_start)
            overlap_end   = min(endTime, s_end)
            if overlap_start < overlap_end:
                self.double.append((overlap_start, overlap_end))

        # 3) Record the event itself as a single booking.
        self.single.append((startTime, endTime))
        return True