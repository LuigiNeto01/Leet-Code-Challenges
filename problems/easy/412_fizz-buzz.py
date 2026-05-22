from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        # Iterate from 1 to n (inclusive, 1-indexed)
        for i in range(1, n + 1):
            # Check divisibility by both 3 and 5 first (divisible by 15)
            if i % 15 == 0:
                answer.append("FizzBuzz")
            # Check divisibility by 3 only
            elif i % 3 == 0:
                answer.append("Fizz")
            # Check divisibility by 5 only
            elif i % 5 == 0:
                answer.append("Buzz")
            # Not divisible by 3 or 5
            else:
                answer.append(str(i))
        
        return answer