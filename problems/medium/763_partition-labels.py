from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # First, record the last occurrence index of each character in the string.
        last_occurrence = {}
        for i, ch in enumerate(s):
            last_occurrence[ch] = i  # later indices overwrite earlier ones, giving the last

        partitions = []  # will hold the sizes of each partition
        segment_start = 0  # start index of the current segment
        segment_end = 0    # current farthest last occurrence within the segment

        # Traverse the string to create partitions greedily.
        for i, ch in enumerate(s):
            # Extend the segment's end if the current character's last occurrence is further.
            segment_end = max(segment_end, last_occurrence[ch])

            # If we've reached the end of the current segment (no character inside
            # appears later), finalize this segment.
            if i == segment_end:
                # Size of the segment is (current index - start + 1)
                partitions.append(i - segment_start + 1)
                # Start a new segment right after this one.
                segment_start = i + 1

        return partitions