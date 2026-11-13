class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # Helper: can we ship all packages within given days using capacity C?
        def can_ship(capacity: int) -> bool:
            total = 0          # weight accumulated on current day
            day_count = 1      # at least one day needed
            for w in weights:
                # If a single package exceeds capacity, impossible
                if w > capacity:
                    return False
                # If adding this package exceeds capacity, start new day
                if total + w > capacity:
                    day_count += 1
                    total = w
                else:
                    total += w
            return day_count <= days

        # The answer is between max(weights) and sum(weights)
        low = max(weights)
        high = sum(weights)

        # Binary search for minimal feasible capacity
        while low < high:
            mid = (low + high) // 2
            if can_ship(mid):
                high = mid   # try smaller capacity
            else:
                low = mid + 1
        return low