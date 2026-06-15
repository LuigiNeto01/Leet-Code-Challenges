class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # Calculate how many test rounds we can perform
        tests = minutesToTest // minutesToDie
        
        # Each pig can be in (tests + 1) states:
        # - dies after round 1, 2, ..., tests, or never dies
        states = tests + 1
        
        # We need minimum pigs such that states^pigs >= buckets
        # This is equivalent to: pigs >= log_states(buckets)
        # Which means: pigs = ceil(log(buckets) / log(states))
        
        pigs = 0
        # Keep adding pigs until we can distinguish all buckets
        while states ** pigs < buckets:
            pigs += 1
        
        return pigs