class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        digits_set = sorted([int(d) for d in digits])
        n_str = str(n)
        len_n = len(n_str)
        
        count = 0
        for i in range(1, len_n):
            count += len(digits_set) ** i
        
        for i, char in enumerate(n_str):
            current_digit = int(char)
            smaller_count = sum(1 for d in digits_set if d < current_digit)
            remaining_positions = len_n - i - 1
            count += smaller_count * (len(digits_set) ** remaining_positions)
            
            if current_digit not in digits_set:
                break
            
            if i == len_n - 1:
                count += 1
        
        return count