class StockSpanner:

    def __init__(self):
        # Stack stores pairs (price, span) for strictly decreasing prices.
        # The span is the number of consecutive past days covered by that price.
        self.stack = []

    def next(self, price: int) -> int:
        # Today's span starts at 1 (the current day itself).
        span = 1

        # While the previous price is <= today's price, that day's span
        # is part of today's consecutive span. Add it and remove it.
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        # Push today's price with its computed span.
        self.stack.append((price, span))

        return span