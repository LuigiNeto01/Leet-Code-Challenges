from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Sort courses by deadline (lastDay) so we consider earliest deadlines first
        courses.sort(key=lambda x: x[1])

        # Max-heap using negative values to store durations of taken courses
        heap = []
        total_time = 0

        for duration, last_day in courses:
            # Tentatively take this course
            heapq.heappush(heap, -duration)  # push negative for max-heap
            total_time += duration

            # If total time exceeds current deadline, drop the longest course
            if total_time > last_day:
                # Remove the course with largest duration
                longest = -heapq.heappop(heap)
                total_time -= longest

        # The heap size equals the maximum number of courses we can finish
        return len(heap)