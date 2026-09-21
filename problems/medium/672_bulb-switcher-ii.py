class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # The state of each bulb depends on its label modulo 2 and modulo 3.
        # Therefore the entire configuration repeats every lcm(2,3)=6 bulbs.
        # So we only need to consider the first min(n, 6) bulbs to determine uniqueness.
        pattern_len = n if n < 6 else 6

        seen = set()

        # Enumerate all 2^4 = 16 parity patterns for the four buttons.
        for a in (0, 1):
            for b in (0, 1):
                for c in (0, 1):
                    for d in (0, 1):
                        total_parity = a + b + c + d
                        # We need exactly `presses` presses.
                        # The minimal number of presses to achieve this parity is total_parity.
                        # The remaining presses must be an even number (they cancel in pairs).
                        if presses >= total_parity and (presses - total_parity) % 2 == 0:
                            # Build the state pattern for the first pattern_len bulbs.
                            state = []
                            for i in range(1, pattern_len + 1):
                                # Start from 1 (on). XOR with each button effect.
                                val = 1
                                val ^= a                     # button 1: flip all
                                if i % 2 == 0:
                                    val ^= b                # button 2: flip even
                                else:
                                    val ^= c                # button 3: flip odd
                                if i % 3 == 1:
                                    val ^= d                # button 4: flip labels 1,4,7,...
                                state.append(val)
                            seen.add(tuple(state))

        return len(seen)