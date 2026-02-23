class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # Use two rand7() calls to generate one of 49 equally likely values
        # Map the first 40 outcomes to 1..10, discard the rest (rejection sampling)
        while True:
            a = rand7()  # 1..7
            b = rand7()  # 1..7
            idx = (a - 1) * 7 + b  # maps (a,b) to 1..49 uniformly
            if idx <= 40:
                # Uniformly map 1..40 to 1..10
                return (idx - 1) % 10 + 1