class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        # Track the count of $5 and $10 bills we have in hand
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                # No change needed, just collect the $5
                five += 1
            elif bill == 10:
                # Need to give back $5 change; must have at least one $5
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                # Need $15 change. Prefer using $10 + $5 to keep more $5s
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True