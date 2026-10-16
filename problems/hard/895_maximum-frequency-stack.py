from collections import defaultdict


class FreqStack:

    def __init__(self):
        # freq[val] = current frequency of val
        self.freq = {}
        # groups[f] = stack of values that have reached frequency f
        self.groups = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f

        # Add val to the stack corresponding to its new frequency
        self.groups[f].append(val)

        if f > self.max_freq:
            self.max_freq = f

    def pop(self) -> int:
        # The top of the max-frequency stack is the most recently pushed
        # element among all elements with the maximum frequency.
        val = self.groups[self.max_freq].pop()
        self.freq[val] -= 1

        # If no element has the old max frequency anymore, decrease it.
        if not self.groups[self.max_freq]:
            self.max_freq -= 1

        return val