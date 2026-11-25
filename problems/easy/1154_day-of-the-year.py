class Solution:
    def dayOfYear(self, date: str) -> int:
        # Split the input string into year, month, and day
        parts = date.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        
        # Days in each month for a common year (index 0 = January)
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Account for leap year: February has 29 days instead of 28
        # Leap year rule: divisible by 400 OR (divisible by 4 AND not by 100)
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days_in_month[1] = 29  # February gets an extra day
        
        # Sum all days from months before the current month
        day_number = 0
        for m in range(month - 1):  # iterate from January to month-1
            day_number += days_in_month[m]
        
        # Add the days of the current month
        day_number += day
        
        return day_number