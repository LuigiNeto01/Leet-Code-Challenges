from collections import Counter
from collections import defaultdict
from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # Count frequency of each number
        freq = Counter(nums)
        # 'need[x]' = how many subsequences ending at x-1 we can extend with x
        need = defaultdict(int)

        for x in nums:
            if freq[x] == 0:
                # Already used by earlier operations
                continue

            if need[x] > 0:
                # Append x to an existing subsequence that ends at x-1
                need[x] -= 1
                need[x + 1] += 1
                freq[x] -= 1
            else:
                # Start a new subsequence: need x, x+1, x+2
                if freq[x + 1] > 0 and freq[x + 2] > 0:
                    freq[x] -= 1
                    freq[x + 1] -= 1
                    freq[x + 2] -= 1
                    # The new subsequence now ends at x+2, can be extended by x+3
                    need[x + 3] += 1
                else:
                    return False

        return True