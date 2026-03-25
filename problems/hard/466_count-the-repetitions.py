class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # If s2 contains a character not present in s1 at all,
        # matching even one copy of s2 is impossible.
        if set(s2) - set(s1):
            return 0

        len2 = len(s2)

        # j: current position inside s2 that we are trying to match next.
        # s2_count: how many full s2 strings have been matched so far.
        j = 0
        s2_count = 0

        # For each finished block of s1, remember the state of j.
        # If the same j appears again, the process from there will repeat,
        # so we can jump over many remaining blocks at once.
        seen = {}

        # Record prefix totals after each processed s1 block.
        # count_after[i] = number of full s2 matched after i blocks of s1.
        count_after = [0] * (n1 + 1)

        for block in range(1, n1 + 1):
            # Greedily consume one whole s1 block against the current s2 pointer.
            for ch in s1:
                if ch == s2[j]:
                    j += 1
                    # Completing one s2 means we start matching the next copy.
                    if j == len2:
                        j = 0
                        s2_count += 1

            count_after[block] = s2_count

            # Same s2 pointer means the future evolution repeats exactly.
            if j in seen:
                prev_block = seen[j]
                prefix_s2 = count_after[prev_block]

                # Cycle spans from prev_block+1 ... block.
                cycle_blocks = block - prev_block
                cycle_s2 = s2_count - prefix_s2

                # Total blocks remaining after the prefix.
                remaining_blocks = n1 - prev_block

                # Use as many full cycles as possible.
                full_cycles = remaining_blocks // cycle_blocks
                total_s2 = prefix_s2 + full_cycles * cycle_s2

                # Handle the tail blocks that do not fill a complete cycle.
                tail_blocks = remaining_blocks % cycle_blocks
                total_s2 += count_after[prev_block + tail_blocks] - count_after[prev_block]

                # Each answer unit needs n2 full copies of s2.
                return total_s2 // n2

            seen[j] = block

        # No cycle found within n1 blocks; use the direct total.
        return s2_count // n2