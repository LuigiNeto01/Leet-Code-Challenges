from __future__ import annotations

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Words for 1-19
        less_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                   "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                   "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                   "Nineteen"]
        # Tens multiples
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                "Seventy", "Eighty", "Ninety"]

        # Helper to convert numbers < 100 to words
        def two(n: int) -> str:
            if n == 0:
                return ""
            if n < 20:
                return less_20[n]
            t = n // 10
            r = n % 10
            if r:
                return tens[t] + " " + less_20[r]
            return tens[t]

        # Helper to convert numbers < 1000 to words
        def three(n: int) -> str:
            parts = []
            if n >= 100:
                parts.append(less_20[n // 100])
                parts.append("Hundred")
                n %= 100
            if n:
                w = two(n)
                if w:
                    parts.append(w)
            return " ".join(parts)

        result_parts = []

        # Break the number into billions, millions, thousands, and the last part
        billions = num // 1_000_000_000
        if billions:
            result_parts.append(three(billions) + " Billion")
        num %= 1_000_000_000

        millions = num // 1_000_000
        if millions:
            result_parts.append(three(millions) + " Million")
        num %= 1_000_000

        thousands = num // 1_000
        if thousands:
            result_parts.append(three(thousands) + " Thousand")
        num %= 1_000

        if num:
            result_parts.append(three(num))

        return " ".join(result_parts)