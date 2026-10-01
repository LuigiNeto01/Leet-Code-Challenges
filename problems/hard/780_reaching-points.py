class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # If target is below starting point in any dimension, impossible (only increase).
        if tx < sx or ty < sy:
            return False
        
        # Work backwards from the target to the start.
        # While both coordinates are larger than the starting ones,
        # reduce the larger one by multiples of the smaller one (modulo).
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        
        # After the reduction, at least one coordinate matches the start.
        # The remaining difference on the other coordinate must be a multiple
        # of the start coordinate, because only repeated addition of that
        # coordinate could close the gap.
        if tx == sx:
            return (ty - sy) % sx == 0
        if ty == sy:
            return (tx - sx) % sy == 0
        
        # If no coordinate matches, the target is unreachable.
        return False