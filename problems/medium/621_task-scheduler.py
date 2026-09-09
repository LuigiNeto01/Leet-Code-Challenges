from __future__ import annotations
from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        freq = Counter(tasks)
        
        # Find the task with maximum frequency
        max_freq = max(freq.values())
        
        # Count how many tasks have this maximum frequency
        max_count = sum(1 for count in freq.values() if count == max_freq)
        
        # Formula explanation:
        # The most frequent task(s) will create the frame.
        # We need (max_freq - 1) gaps of length (n + 1) to separate them,
        # plus the max_count tasks that appear at the end.
        # Formula: (max_freq - 1) * (n + 1) + max_count
        # If this is less than total tasks, it means no idle needed.
        total_tasks = len(tasks)
        min_intervals = (max_freq - 1) * (n + 1) + max_count
        
        # Cannot be less than total tasks (when n is small)
        return max(min_intervals, total_tasks)