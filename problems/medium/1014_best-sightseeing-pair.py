class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        """
        Maximize values[i] + values[j] + i - j for i < j.
        Rewrite as (values[i] + i) + (values[j] - j).
        Keep track of best 'values[i] + i' seen so far.
        """
        # Initialize best_i with the first element's value + its index
        best_i = values[0] + 0
        max_score = float('-inf')  # Use -inf to handle negative scores (though problem says values >=1)
        
        # Iterate j from index 1 to end
        for j in range(1, len(values)):
            # Current candidate score using best_i and current j
            candidate = best_i + (values[j] - j)
            # Update global maximum
            if candidate > max_score:
                max_score = candidate
            # Update best_i for future j: include current j as potential i
            current_i = values[j] + j
            if current_i > best_i:
                best_i = current_i
        
        return max_score