class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Reference: 1971-01-01 is Friday.
        # Map index 0..6 to day names (Sunday..Saturday)
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        def is_leap(y: int) -> bool:
            # Leap year if divisible by 400, or divisible by 4 but not by 100
            return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

        # Days in each month for a common year (index 0 = January)
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        total_days = 0

        # Count days in full years before the given year
        for y in range(1971, year):
            total_days += 366 if is_leap(y) else 365

        # Count days in months of the current year before the given month
        for m in range(1, month):
            days_in_month = month_days[m - 1]
            # February of a leap year has 29 days
            if m == 2 and is_leap(year):
                days_in_month = 29
            total_days += days_in_month

        # Add days in the current month (day is 1-indexed, subtract 1 to get offset)
        total_days += day - 1

        # 1971-01-01 (total_days = 0) is Friday -> index 5 in our list
        day_index = (total_days + 5) % 7
        return days_of_week[day_index]