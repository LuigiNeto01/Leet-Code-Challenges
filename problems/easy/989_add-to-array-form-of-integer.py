class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        # We will add digit by digit from the least significant end.
        result = []               # stores digits in reverse order (least significant first)
        carry = 0
        i = len(num) - 1          # pointer to current digit in num (rightmost)

        # Continue while there are digits in num, remaining k, or leftover carry
        while i >= 0 or k > 0 or carry > 0:
            # digit from num, or 0 if we have exhausted num
            digit_num = num[i] if i >= 0 else 0
            # last digit of k
            digit_k = k % 10

            # sum of current column plus carry
            total = digit_num + digit_k + carry
            # digit to put in this position
            result.append(total % 10)
            # carry for the next higher place
            carry = total // 10

            # update pointers and k
            k //= 10              # remove the last digit we just used
            i -= 1                # move left in num

        # result was built from least significant digit; reverse for correct order
        return result[::-1]