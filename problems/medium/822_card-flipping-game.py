class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        # Step 1: track numbers that appear on both sides of the same card (front == back)
        # These numbers can never become "good" because they will always be facing up on that card
        same = set()
        for f, b in zip(fronts, backs):
            if f == b:
                same.add(f)

        # Step 2: collect all distinct numbers that appear on any card (either side
        # (Numbers that appear only on different sides can be flipped to make them down)
        all_nums = set()
        for num in fronts:
            all_nums.add(num)
        for num in backs:
            all_nums.add(num)

        # Step 3: good numbers are those that appear on any card but never in a "same" card
        good_mins = [x for x in all_nums if x not in same]
        return min(good_mins) if good_mins else 0